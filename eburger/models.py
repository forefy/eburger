from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union
import re


def prettify_path(path: str) -> str:
    return re.sub(r"^(\.\./|\./)+", "", path)


@dataclass
class ASTNode:
    """
    Represents a generic node in an Abstract Syntax Tree (AST).

    An ASTNode is a fundamental part of representing the structure of a
    programming language's source code, used extensively in compilers and
    code analysis tools.

    Attributes:
        node_id: int - A unique identifier for the node within the AST.
        node_type: str - The type of the node (e.g., 'SourceUnit', 'PragmaDirective').
        src: str - Source location for this node within its file.
        children: List[ASTNode] - Child nodes of this AST node.

    Methods:
        add_child - Adds a child node to this node's children.
    """

    node_id: int
    node_type: str
    src: str
    children: List["ASTNode"]

    def add_child(self, child: "ASTNode"):
        """Adds a child AST node to the current node."""
        self.children.append(child)

    def get_display_name(self):
        return f"{self.node_type} {self.node_id}"


@dataclass
class SourceUnit(ASTNode):
    """
    Represents a Source Unit node in an AST for Solidity source code.

    A Source Unit typically represents a single Solidity source file and is the
    root node for the AST of that file. It contains metadata about the file, like
    licensing information, and serves as the container for all top-level declarations
    in the file.

    Attributes:
        license: str - License information for the source file, if available.
        exported_symbols: Dict[str, List[int]] - A mapping of exported symbols and
                         their respective positions within the source file.
    """

    absolute_path: str
    license: str
    exported_symbols: Dict[str, List[int]] = field(default_factory=dict)

    def get_display_name(self):
        display_name = self.node_type
        if self.absolute_path is not None:
            display_name += f" {prettify_path(self.absolute_path)}"
        return display_name


@dataclass
class PragmaDirective(ASTNode):
    """
    Represents a Pragma Directive in a Solidity source file.

    Pragma Directives are used to specify compiler instructions or configurations,
    most commonly the compiler version. For example, `pragma solidity ^0.8.0;`
    indicates that the Solidity file should be compiled with a compiler version
    greater than or equal to 0.8.0 but less than 0.9.0.

    Attributes:
        literals: List[str] - The components of the pragma directive,
                  e.g., ['solidity', '^', '0.8', '.0'] for `pragma solidity ^0.8.0;`.
    """

    literals: List[str] = field(default_factory=list)


@dataclass
class Identifier(ASTNode):
    """
    Represents an Identifier node in a Solidity source file.

    An Identifier node typically refers to names of variables, functions,
    contracts, libraries, etc., within the Solidity code.

    Attributes:
        name: str - The name of the identifier.
        overloaded_declarations: List[int] - A list of declaration IDs if the identifier is overloaded.
        type_descriptions: Dict - Type descriptions for the identifier.
    """

    name: str
    overloaded_declarations: List[int] = field(default_factory=list)
    referenced_declaration: int = None
    type_descriptions: Dict = field(default_factory=dict)

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class SymbolAlias:
    """
    Represents an alias in an Import Directive, mapping a foreign identifier to a local name.

    Attributes:
        foreign: Identifier - The foreign identifier being imported.
        name_location: str - The location of the alias name in the source file.
    """

    foreign: Identifier
    name_location: str


@dataclass
class ImportDirective(ASTNode):
    """
    Represents an Import Directive in a Solidity source file.

    Import Directives are used in Solidity to include code from other files,
    similar to import statements in other programming languages. This is essential
    for code reusability and organization, allowing the use of libraries, contracts,
    and other constructs from separate files.

    Attributes:
        file: str - The path of the file being imported.
        name_location: str - The location of the name in the source file, typically "-1:-1:-1" for imports.
        scope: int - The scope in which this import is valid. Usually refers to the ID of the parent node.
        source_unit: int - The ID of the source unit that this import refers to.
        src: str - Source location for this node within its file.
        symbol_aliases: List[str] - A list of aliases for symbols imported from the file.
        unit_alias: str - An alias for the unit being imported, if any.
    """

    file: str
    name_location: str
    scope: int
    source_unit: int
    unit_alias: str
    symbol_aliases: List[SymbolAlias]
    absolute_path: str = None

    def get_display_name(self):
        return f"{self.node_type} {prettify_path(self.file)}"


@dataclass
class ContractDefinition(ASTNode):
    """
    Represents a Contract Definition in a Solidity source file.

    This node type can represent a contract, an interface, or a library. It includes
    details such as the contract's kind, its documentation, and its dependencies.

    Attributes:
        abstract: bool - Indicates whether the contract is abstract.
        base_contracts: List[int] - Node IDs of the contract's base contracts.
        contract_dependencies: List[int] - Node IDs of contracts that this contract depends on.
        contract_kind: str - The kind of contract (e.g., 'contract', 'interface', 'library').
        fully_implemented: bool - Indicates whether the contract is fully implemented.
        linearized_base_contracts: List[int] - A linearized list of base contracts,
                                  important for understanding inheritance hierarchies.
        name: str - The name of the contract.
        name_location: str - Location of the contract name in the source file.
        nodes: List[ASTNode] - Child nodes (like functions, state variables) of the contract.
        scope: int - The scope ID where this contract is defined.
        used_errors: List[int] - Node IDs of errors used by the contract.
    """

    abstract: bool
    base_contracts: List[int]
    contract_dependencies: List[int]
    contract_kind: str
    fully_implemented: bool
    linearized_base_contracts: List[int]
    name: str
    name_location: str
    scope: int
    used_errors: List[int]
    nodes: List[ASTNode] = field(default_factory=dict)

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class LiteralValue(ASTNode):
    """
    Represents a Literal value in a Solidity source file.

    Literals are constant values directly written in the source code, such as numbers, strings, or boolean values.

    Attributes:
        hex_value: str - The hexadecimal representation of the value, if applicable.
        is_constant: bool - Indicates if the literal is a constant value.
        is_lvalue: bool - Indicates if the literal can be assigned to (left-value).
        is_pure: bool - Indicates if the literal is a pure value (has no side effects).
        kind: str - The kind of literal (e.g., 'number', 'string').
        lvalue_requested: bool - Indicates if an l-value has been requested for this literal.
        subdenomination: str - The subdenomination of the value, if any (e.g., 'wei', 'gwei' for Ether values).
        type_descriptions: Dict - Descriptions of the literal's type.
        value: str - The value of the literal in string format.
    """

    hex_value: str
    is_constant: bool
    is_lvalue: bool
    is_pure: bool
    kind: str
    lvalue_requested: bool
    type_descriptions: Dict
    value: str
    subdenomination: str = None

    def get_display_name(self):
        return f"{self.node_type} {self.value}"


@dataclass
class VariableDeclaration(ASTNode):
    """
    Represents a Variable Declaration in a Solidity source file.

    This class is used for declaring both state variables in contracts and parameters in functions.
    Certain attributes may only be relevant in specific contexts (e.g., 'stateVariable' is used
    for state variables, 'functionSelector' is applicable to certain state variables).

    Attributes:
        constant: bool - Indicates if the variable is constant.
        function_selector: Optional[str] - The unique selector for the variable, if applicable.
        mutability: str - The mutability of the variable (e.g., 'mutable', 'constant').
        name: str - The name of the variable.
        scope: int - The scope ID where this variable is defined.
        src: str - Source location for this node within its file.
        state_variable: bool - Indicates if it is a state variable.
        storage_location: str - The storage location of the variable (e.g., 'storage', 'memory').
        type_descriptions: Dict - Descriptions of the variable's type.
        typeName: TypeName - The type of the variable.
        value: Optional[LiteralValue] - The value of the variable, if any.
        visibility: str - The visibility of the variable (e.g., 'public', 'internal').
    """

    constant: bool
    mutability: str
    name: str
    scope: int
    src: str
    state_variable: bool
    storage_location: str
    type_descriptions: Dict
    visibility: str
    indexed: bool = None
    function_selector: Optional[str] = None
    typeName: Dict = field(default_factory=dict)
    value: Optional[LiteralValue] = None

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class ParameterList(ASTNode):
    """
    Represents a list of parameters in a Solidity function.

    This is used for representing both the input parameters and return parameters
    of a function.

    Attributes:
        parameters: List[VariableDeclaration] - A list of variable declarations representing the parameters.
    """

    parameters: List[ASTNode] = field(default_factory=list)


@dataclass
class Block(ASTNode):
    statements: List[ASTNode]


@dataclass
class FunctionDefinition(ASTNode):
    """
    Represents a Function Definition in a Solidity source file.

    This node type includes details about a function such as its parameters,
    return types, visibility (public, external, etc.), state mutability
    (payable, view, pure, etc.), and any attached documentation.

    Attributes:
        function_selector: str - The unique selector for the function.
        implemented: bool - Indicates whether the function is implemented.
        kind: str - The kind of function (e.g., function, constructor).
        modifiers: List[int] - Node IDs of the modifiers applied to the function.
        name: str - The name of the function.
        parameters: ParameterList - The list of parameters for the function.
        return_parameters: ParameterList - The list of return parameters for the function.
        scope: int - The scope ID where this function is defined.
        state_mutability: str - The state mutability of the function (e.g., payable, nonpayable).
        virtual: bool - Indicates whether the function is virtual.
        visibility: str - The visibility of the function (e.g., public, external).
    """

    function_selector: str
    kind: str
    modifiers: List[int]
    name: str
    parameters: ParameterList
    return_parameters: ParameterList
    scope: int
    state_mutability: str
    virtual: bool
    visibility: str
    body: Block
    name_location: str = None
    implemented: bool = None

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class IdentifierPath(ASTNode):
    """
    Represents an identifier path in Solidity, typically used for names of contracts,
    libraries, and other identifiers.

    Attributes:
        name: str - The name of the identifier.
        referencedDeclaration: int - The declaration ID that this identifier refers to.
    """

    name: str
    referencedDeclaration: int

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class UserDefinedTypeName(ASTNode):
    """
    Represents a user-defined type name in Solidity, like contract names or new types defined by the user.

    Attributes:
        pathNode: IdentifierPath - The path node representing the type name.
        referencedDeclaration: int - The declaration ID of the type.
    """

    pathNode: IdentifierPath
    referencedDeclaration: int


@dataclass
class UsingForDirective(ASTNode):
    """
    Represents a Using For Directive in a Solidity source file.

    This directive is used to attach library functions to a specific type.
    For example, `using SafeMath for uint;` allows the functions from the
    SafeMath library to be called on uint types.

    Attributes:
        libraryName: IdentifierPath - The name of the library being used.
        typeName: UserDefinedTypeName - The type that the library is being used for.
    """

    libraryName: IdentifierPath
    typeName: UserDefinedTypeName


@dataclass
class ErrorDefinition(ASTNode):
    """
    Represents an Error Definition in a Solidity source file.

    Custom errors are defined using the 'error' keyword and can be used for
    efficient error handling and reporting in contracts.

    Attributes:
        name: str - The name of the error.
        parameters: ParameterList - The list of parameters for the error.
    """

    name: str
    parameters: ParameterList

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class EventDefinition(ASTNode):
    """
    Represents an Event Definition in a Solidity source file.

    Events are used for logging and can be emitted in contracts to signal and record actions.

    Attributes:
        anonymous: bool - Indicates if the event is anonymous.
        name: str - The name of the event.
        parameters: ParameterList - The list of parameters for the event.
    """

    anonymous: bool
    name: str
    parameters: ParameterList

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class ModifierDefinition(ASTNode):
    """
    Represents a Modifier Definition in a Solidity source file.

    Modifiers are reusable components that modify the behavior of functions.

    Attributes:
        name: str - The name of the modifier.
        name_location: str - Location of the modifier name in the source file.
        parameters: ParameterList - The list of parameters for the modifier.
        body: Block - The body of the modifier.
        virtual: bool - Indicates whether the modifier is virtual.
        visibility: str - The visibility of the modifier (e.g., 'public', 'internal').
    """

    name: str
    name_location: str
    parameters: ParameterList
    body: Block
    virtual: bool
    visibility: str

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class Assignment(ASTNode):
    """
    Represents an Assignment operation in a Solidity source file.

    An Assignment operation assigns a value to a variable.

    Attributes:
        left_hand_side: Identifier - The variable being assigned to.
        operator: str - The assignment operator (usually '=').
        right_hand_side: Union[Identifier, LiteralValue] - The value being assigned.
        type_descriptions: Dict[str, str] - Type descriptions of the assignment.
    """

    left_hand_side: Identifier
    operator: str
    right_hand_side: Union[Identifier, LiteralValue]
    type_descriptions: Dict[str, str]

    def get_display_name(self):
        return f"{self.node_type} {self.left_hand_side.get_display_name()} {self.operator} {self.right_hand_side.get_display_name()}"


@dataclass
class ExpressionStatement(ASTNode):
    """
    Represents an Expression Statement in a Solidity source file.

    Expression Statements are typically used for expressions that have side effects.

    Attributes:
        expression: Assignment - The expression in the statement.
    """

    expression: Assignment


@dataclass
class FunctionCall(ASTNode):
    """
    Represents a Function Call in a Solidity source file.

    Function Calls are expressions that call a function.

    Attributes:
        arguments: List[Union[Identifier, LiteralValue]] - Arguments passed to the function.
        expression: Identifier - The function being called.
        is_constant: bool - Indicates if the function call is constant.
        is_lvalue: bool - Indicates if the function call can be assigned to (left-value).
        is_pure: bool - Indicates if the function call is pure (has no side effects).
        kind: str - The kind of function call.
        lvalue_requested: bool - Indicates if an l-value has been requested for this function call.
        type_descriptions: Dict[str, str] - Type descriptions of the function call.
    """

    arguments: List[Union[Identifier, LiteralValue]]
    expression: Identifier
    is_constant: bool
    is_lvalue: bool
    is_pure: bool
    kind: str
    lvalue_requested: bool
    type_descriptions: Dict[str, str]

    def get_display_name(self):
        return f"{self.node_type} {self.node_id}"


@dataclass
class EmitStatement(ASTNode):
    """
    Represents an Emit Statement in a Solidity source file.

    Emit Statements are used to emit events.

    Attributes:
        event_call: FunctionCall - The function call that emits the event.
    """

    event_call: FunctionCall


@dataclass
class IfStatement(ASTNode):
    """
    Represents an If Statement in a Solidity source file.

    If Statements are used for conditional execution of code blocks.

    Attributes:
        condition: ASTNode - The condition being evaluated.
        trueBody: ASTNode - The body of the statement if the condition is true.
        falseBody: Optional[ASTNode] - The body of the statement if the condition is false.
    """

    condition: ASTNode
    trueBody: ASTNode
    falseBody: Optional[ASTNode] = None


@dataclass
class ReturnValue(ASTNode):
    """
    Represents a Return Statement in a Solidity source file.

    Return Statements are used to return values from functions.

    Attributes:
        expression: Optional[ASTNode] - The expression being returned.
        functionReturnParameters: int - ID of the return parameter list.
    """

    expression: Optional[ASTNode]
    functionReturnParameters: int


@dataclass
class BinaryOperation(ASTNode):
    """
    Represents a Binary Operation in a Solidity source file.

    Binary Operations include arithmetic, logical, and relational operations.

    Attributes:
        leftExpression: ASTNode - The left operand of the binary operation.
        operator: str - The operator of the binary operation.
        rightExpression: ASTNode - The right operand of the binary operation.
    """

    leftExpression: ASTNode
    operator: str
    rightExpression: ASTNode

    def get_display_name(self):
        return f"{self.node_type} {self.leftExpression.get_display_name()} {self.operator} {self.rightExpression.get_display_name()}"


@dataclass
class VariableDeclarationStatement(ASTNode):
    """
    Represents a Variable Declaration Statement in a Solidity source file.

    This statement is used for declaring and optionally initializing variables.

    Attributes:
        declarations: List[VariableDeclaration] - The variables being declared.
        assignments: List[int] - Node IDs where this variable is assigned.
        initialValue: Optional[ASTNode] - Initial value assigned to the variable, if any.
    """

    declarations: List[VariableDeclaration]
    assignments: List[int]
    initialValue: Optional[ASTNode] = None


@dataclass
class ElementaryTypeName(ASTNode):
    """
    Represents an Elementary Type Name in a Solidity source file.

    Elementary Type Names include basic types like int, uint, bool, address, etc.

    Attributes:
        name: str - The name of the elementary type.
        type_descriptions: Dict[str, str] - Additional type descriptions.
    """

    name: str
    type_descriptions: Dict[str, str]

    def get_display_name(self):
        return f"{self.node_type} {self.name}"


@dataclass
class ElementaryTypeNameExpression(ASTNode):
    """
    Represents an Elementary Type Name Expression in a Solidity source file.

    This type of expression is often used in casting to a basic type.

    Attributes:
        typeName: ElementaryTypeName - The type to which the expression is referring.
        argumentTypes: List[Dict[str, str]] - Argument types for the expression.
        is_pure: bool - Indicates if the expression is pure.
    """

    typeName: ElementaryTypeName
    argumentTypes: List[Dict[str, str]]
    is_pure: bool


@dataclass
class RevertStatement(ASTNode):
    """
    Represents a Revert Statement in a Solidity source file.

    Revert Statements are used to revert the entire transaction, optionally returning an error.

    Attributes:
        errorCall: FunctionCall - The function call that triggers the revert, typically an error.
    """

    errorCall: FunctionCall


@dataclass
class MemberAccess(ASTNode):
    """
    Represents a Member Access operation in a Solidity source file.

    Member Access is used to access properties or methods of an object or type.

    Attributes:
        expression: Identifier - The object or type being accessed.
        memberName: str - The name of the member (property or method) being accessed.
        type_descriptions: Dict[str, str] - Type descriptions of the member being accessed.
    """

    expression: Identifier
    memberName: str
    type_descriptions: Dict[str, str]

    def get_display_name(self):
        return f"{self.node_type} {self.memberName}"


@dataclass
class Conditional(ASTNode):
    """
    Represents a Conditional (ternary) operation in a Solidity source file.

    The Conditional node evaluates a condition and returns one of two expressions based on the condition's truthiness.

    Attributes:
        condition: ASTNode - The condition being evaluated.
        trueExpression: ASTNode - The expression returned if the condition is true.
        falseExpression: ASTNode - The expression returned if the condition is false.
        type_descriptions: Dict[str, str] - Type descriptions of the conditional expression.
    """

    condition: ASTNode
    trueExpression: ASTNode
    falseExpression: ASTNode
    type_descriptions: Dict[str, str]


@dataclass
class TupleExpression(ASTNode):
    """
    Represents a Tuple Expression in a Solidity source file.

    Tuple Expressions are used to group multiple values into a single compound value.

    Attributes:
        components: List[ASTNode] - A list of expressions or declarations that form the components of the tuple.
        type_descriptions: Dict[str, str] - Type descriptions of the tuple expression.
    """

    components: List[ASTNode]
    type_descriptions: Dict[str, str]


@dataclass
class IndexAccess(ASTNode):
    """
    Represents an Index Access operation in a Solidity source file.

    Index Access is used for accessing elements of a mapping or an array by a key or an index.

    Attributes:
        baseExpression: Identifier - The base mapping or array being accessed.
        indexExpression: Identifier - The index or key used to access the element.
        type_descriptions: Dict[str, str] - Type descriptions of the accessed element.
    """

    baseExpression: Identifier
    indexExpression: Identifier
    type_descriptions: Dict[str, str]


@dataclass
class UnaryOperation(ASTNode):
    is_constant: bool
    is_lvalue: bool
    is_pure: bool
    lvalue_requested: bool
    type_descriptions: Dict
    operator: str
    prefix: bool
    src: str
    subExpression: IndexAccess


@dataclass
class ForStatement(ASTNode):
    """
    Represents a 'for' statement in a Solidity source file.

    Attributes:
        initializationExpression: VariableDeclarationStatement - The initialization expression of the for loop.
        condition: ASTNode - The condition expression of the for loop.
        loopExpression: ExpressionStatement - The loop expression (increment/decrement) of the for loop.
        body: Block - The body of the for loop.
        node_id: int - A unique identifier for the node within the AST.
        src: str - Source location for this node within its file.
    """

    initializationExpression: Optional[VariableDeclarationStatement]
    condition: Optional[ASTNode]
    loopExpression: Optional[ExpressionStatement]
    body: Block
    node_id: int
    src: str


@dataclass
class FunctionCallOptions(ASTNode):
    """
    Represents function call options in a Solidity source file.

    Attributes:
        expression: ASTNode - The expression representing the function being called.
        options: List[Identifier] - The list of options used in the function call.
        names: List[str] - The names of the options.
        typeDescriptions: TypeDescriptions - Type descriptions for the function call.
    """

    expression: ASTNode
    options: List[Identifier]  # Assuming Identifier is already defined
    names: List[str]
    typeDescriptions: Dict = field(default_factory=dict)
    src: str
