from eburger import settings
from eburger.models import (
    ASTNode,
    Assignment,
    BinaryOperation,
    Block,
    Conditional,
    ContractDefinition,
    ElementaryTypeName,
    ElementaryTypeNameExpression,
    EmitStatement,
    ErrorDefinition,
    EventDefinition,
    ExpressionStatement,
    ForStatement,
    FunctionCall,
    FunctionCallOptions,
    FunctionDefinition,
    Identifier,
    IdentifierPath,
    IfStatement,
    ImportDirective,
    IndexAccess,
    LiteralValue,
    ReturnValue,
    MemberAccess,
    ModifierDefinition,
    ParameterList,
    RevertStatement,
    SourceUnit,
    PragmaDirective,
    SymbolAlias,
    TupleExpression,
    UnaryOperation,
    UserDefinedTypeName,
    UsingForDirective,
    VariableDeclaration,
    VariableDeclarationStatement,
)
from eburger.utils.logger import log


def parse_ast_node(node_dict, G, parent=None):
    """
    Parses an AST node and creates an instance of the corresponding Python class.
    """
    absolute_path = node_dict.get("absolutePath")
    exported_symbols = node_dict.get("exportedSymbols", {})
    node_id = node_dict.get("id", 0)
    license = node_dict.get("license")
    node_type = node_dict.get("nodeType")
    child_dicts = node_dict.get("nodes", [])  # List of child node dictionaries
    src = node_dict.get("src")

    match node_type:
        case "SourceUnit":
            parsed_node = SourceUnit(
                absolute_path=absolute_path,
                exported_symbols=exported_symbols,
                node_id=node_id,
                license=license,
                node_type=node_type,
                src=src,
                children=[],
            )

        case "PragmaDirective":
            parsed_node = PragmaDirective(
                node_id=node_id,
                node_type=node_type,
                literals=node_dict.get("literals", []),
                src=src,
                children=[],
            )

        case "ImportDirective":
            symbol_aliases = [
                SymbolAlias(
                    foreign=Identifier(
                        node_id=alias["foreign"].get("id", 0),
                        node_type=alias["foreign"].get("nodeType", ""),
                        name=alias["foreign"].get("name", ""),
                        overloaded_declarations=alias["foreign"].get(
                            "overloadedDeclarations", []
                        ),
                        type_descriptions=alias["foreign"].get("typeDescriptions", {}),
                        src=alias["foreign"].get("src", ""),
                        children=[],
                    ),
                    name_location=alias.get("nameLocation", ""),
                )
                for alias in node_dict.get("symbolAliases", [])
            ]
            parsed_node = ImportDirective(
                node_id=node_dict.get("id", 0),
                node_type=node_type,
                file=node_dict.get("file"),
                name_location=node_dict.get("nameLocation"),
                scope=node_dict.get("scope"),
                source_unit=node_dict.get("sourceUnit"),
                src=node_dict.get("src"),
                symbol_aliases=symbol_aliases,
                unit_alias=node_dict.get("unitAlias", ""),
                children=[],
            )
        case "ContractDefinition":
            parsed_node = ContractDefinition(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType"),
                abstract=node_dict.get("abstract", False),
                base_contracts=node_dict.get("baseContracts", []),
                contract_dependencies=node_dict.get("contractDependencies", []),
                contract_kind=node_dict.get("contractKind", ""),
                fully_implemented=node_dict.get("fullyImplemented", False),
                linearized_base_contracts=node_dict.get("linearizedBaseContracts", []),
                name=node_dict.get("name", ""),
                name_location=node_dict.get("nameLocation", ""),
                scope=node_dict.get("scope", 0),
                src=node_dict.get("src", ""),
                used_errors=node_dict.get("usedErrors", []),
                children=[],
            )
        case "FunctionDefinition":
            # Parsing parameters
            parameters = []
            params_node = node_dict.get("parameters", {}).get("parameters", [])
            for param in params_node:
                parsed_param, G = parse_ast_node(param, G)
                parameters.append(parsed_param)

            # Parsing return parameters
            return_parameters = []
            params_node = node_dict.get("returnParameters", {}).get("parameters", [])
            for param in params_node:
                parsed_param, G = parse_ast_node(param, G)
                return_parameters.append(parsed_param)

            body, G = (
                parse_ast_node(node_dict.get("body", {}), G)
                if "body" in node_dict
                else (None, G)
            )

            parsed_node = FunctionDefinition(
                node_id=node_dict.get("id", 0),
                node_type=node_type,
                function_selector=node_dict.get("functionSelector", ""),
                implemented=node_dict.get("implemented", False),
                kind=node_dict.get("kind", ""),
                modifiers=node_dict.get("modifiers", []),
                name=node_dict.get("name", ""),
                parameters=parameters,
                return_parameters=return_parameters,
                scope=node_dict.get("scope", 0),
                src=node_dict.get("src", ""),
                state_mutability=node_dict.get("stateMutability", ""),
                virtual=node_dict.get("virtual", False),
                visibility=node_dict.get("visibility", ""),
                body=body,
                children=[],
            )

            if body:
                G.add_edge(parsed_node.get_display_name(), body.get_display_name())
            for param in parameters:
                G.add_edge(parsed_node.get_display_name(), param.get_display_name())
            for ret_param in parameters:
                G.add_edge(parsed_node.get_display_name(), ret_param.get_display_name())

        case "VariableDeclaration":
            parsed_node = VariableDeclaration(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                constant=node_dict.get("constant", False),
                function_selector=node_dict.get("functionSelector"),
                mutability=node_dict.get("mutability", ""),
                name=node_dict.get("name", ""),
                scope=node_dict.get("scope", 0),
                src=node_dict.get("src", ""),
                state_variable=node_dict.get("stateVariable", False),
                storage_location=node_dict.get("storageLocation", ""),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                typeName=node_dict.get("typeName", {}),
                visibility=node_dict.get("visibility", ""),
                # Handling optional 'value' field
                value=(
                    LiteralValue(
                        node_id=node_dict.get("value", {}).get("id", 0),
                        node_type=node_dict.get("value", {}).get("nodeType", ""),
                        hex_value=node_dict.get("value", {}).get("hexValue", ""),
                        is_constant=node_dict.get("value", {}).get("isConstant", False),
                        is_lvalue=node_dict.get("value", {}).get("isLValue", False),
                        is_pure=node_dict.get("value", {}).get("isPure", True),
                        kind=node_dict.get("value", {}).get("kind", ""),
                        lvalue_requested=node_dict.get("value", {}).get(
                            "lValueRequested", False
                        ),
                        src=node_dict.get("value", {}).get("src", ""),
                        subdenomination=node_dict.get("value", {}).get(
                            "subdenomination", ""
                        ),
                        type_descriptions=node_dict.get("value", {}).get(
                            "typeDescriptions", {}
                        ),
                        value=node_dict.get("value", {}).get("value", ""),
                        children=[],
                    )
                )
                if "value" in node_dict
                else None,
                children=[],
            )
        case "UsingForDirective":
            library_name_node = node_dict.get("libraryName", {})
            library_name = IdentifierPath(
                node_id=library_name_node.get("id", 0),
                node_type=library_name_node.get("nodeType", ""),
                name=library_name_node.get("name", ""),
                referencedDeclaration=library_name_node.get("referencedDeclaration", 0),
                src=library_name_node.get("src", ""),
                children=[],
            )

            type_name_node = node_dict.get("typeName", {})
            type_name_path_node = type_name_node.get("pathNode", {})
            type_name = UserDefinedTypeName(
                node_id=type_name_node.get("id", 0),
                node_type=type_name_node.get("nodeType", ""),
                pathNode=IdentifierPath(
                    node_id=type_name_path_node.get("id", 0),
                    node_type=type_name_path_node.get("nodeType", ""),
                    name=type_name_path_node.get("name", ""),
                    referencedDeclaration=type_name_path_node.get(
                        "referencedDeclaration", 0
                    ),
                    src=type_name_path_node.get("src", ""),
                    children=[],
                ),
                referencedDeclaration=type_name_node.get("referencedDeclaration", 0),
                src=type_name_node.get("src", ""),
                children=[],
            )

            parsed_node = UsingForDirective(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                src=node_dict.get("src", ""),
                libraryName=library_name,
                typeName=type_name,
                children=[],
            )
        case "ErrorDefinition":
            parameters = []
            params_node = node_dict.get("parameters", {}).get("parameters", [])
            for param in params_node:
                parsed_param, G = parse_ast_node(param, G)
                parameters.append(parsed_param)

            parsed_node = ErrorDefinition(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                name=node_dict.get("name", ""),
                parameters=ParameterList(
                    node_id=node_dict.get("parameters", {}).get("id", 0),
                    node_type=node_dict.get("parameters", {}).get("nodeType", ""),
                    parameters=parameters,
                    src=node_dict.get("parameters", {}).get("src", ""),
                    children=[],
                ),
                src=node_dict.get("src", ""),
                children=[],
            )
            for param in parameters:
                G.add_edge(parsed_node.get_display_name(), param.get_display_name())

        case "EventDefinition":
            parameters = []
            params_node = node_dict.get("parameters", {}).get("parameters", [])
            for param in params_node:
                parsed_param, G = parse_ast_node(param, G)
                parameters.append(parsed_param)

            parsed_node = EventDefinition(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                anonymous=node_dict.get("anonymous", False),
                name=node_dict.get("name", ""),
                parameters=ParameterList(
                    node_id=node_dict.get("parameters", {}).get("id", 0),
                    node_type=node_dict.get("parameters", {}).get("nodeType", ""),
                    parameters=parameters,
                    src=node_dict.get("parameters", {}).get("src", ""),
                    children=[],
                ),
                src=node_dict.get("src", ""),
                children=[],
            )

            for param in parameters:
                G.add_edge(parsed_node.get_display_name(), param.get_display_name())

        case "ModifierDefinition":
            parameters, G = parse_ast_node(node_dict["parameters"], G)
            body, G = parse_ast_node(node_dict["body"], G)
            parsed_node = ModifierDefinition(
                node_id=node_id,
                node_type=node_type,
                name=node_dict.get("name"),
                name_location=node_dict.get("nameLocation"),
                parameters=parameters,
                body=body,
                virtual=node_dict.get("virtual", False),
                visibility=node_dict.get("visibility"),
                src=src,
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), parameters.get_display_name())
            G.add_edge(parsed_node.get_display_name(), body.get_display_name())

        case "Block" | "UncheckedBlock":
            statements = []
            for stmt in node_dict.get("statements", []):
                if stmt:
                    parsed_stmt, G = parse_ast_node(stmt, G)
                    statements.append(parsed_stmt)

            parsed_node = Block(
                node_id=node_id,
                node_type=node_type,
                statements=statements,
                src=src,
                children=[],
            )
            for stmt in statements:
                G.add_edge(parsed_node.get_display_name(), stmt.get_display_name())

        case "Assignment":
            left_hand_side, G = parse_ast_node(node_dict["leftHandSide"], G)
            right_hand_side, G = parse_ast_node(node_dict["rightHandSide"], G)
            parsed_node = Assignment(
                node_id=node_id,
                node_type=node_type,
                left_hand_side=left_hand_side,
                operator=node_dict.get("operator", ""),
                right_hand_side=right_hand_side,
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=src,
                children=[],
            )
            G.add_edge(
                parsed_node.get_display_name(), left_hand_side.get_display_name()
            )
            G.add_edge(
                parsed_node.get_display_name(), right_hand_side.get_display_name()
            )

        case "ExpressionStatement":
            expression, G = parse_ast_node(node_dict["expression"], G)
            parsed_node = ExpressionStatement(
                node_id=node_id,
                node_type=node_type,
                expression=expression,
                src=src,
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), expression.get_display_name())

        case "Identifier":
            parsed_node = Identifier(
                node_id=node_id,
                node_type=node_type,
                name=node_dict.get("name", ""),
                overloaded_declarations=node_dict.get("overloadedDeclarations", []),
                referenced_declaration=node_dict.get("referencedDeclaration", 0),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=src,
                children=[],
            )
        case "FunctionCall":
            arguments = []
            for arg in node_dict.get("arguments", []):
                parsed_arg, G = parse_ast_node(arg, G)
                arguments.append(parsed_arg)
            expression, G = parse_ast_node(node_dict["expression"], G)
            parsed_node = FunctionCall(
                node_id=node_id,
                node_type=node_type,
                arguments=arguments,
                expression=expression,
                is_constant=node_dict.get("isConstant", False),
                is_lvalue=node_dict.get("isLValue", False),
                is_pure=node_dict.get("isPure", False),
                kind=node_dict.get("kind", ""),
                lvalue_requested=node_dict.get("lValueRequested", False),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=src,
                children=[],
            )
            for arg in arguments:
                G.add_edge(parsed_node.get_display_name(), arg.get_display_name())
            G.add_edge(parsed_node.get_display_name(), expression.get_display_name())

        case "EmitStatement":
            event_call, G = parse_ast_node(node_dict["eventCall"], G)
            parsed_node = EmitStatement(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                event_call=event_call,
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), event_call.get_display_name())

        case "PlaceholderStatement":
            parsed_node = ASTNode(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                src=node_dict.get("src", ""),
                children=[],
            )
        case "IfStatement":
            condition, G = parse_ast_node(node_dict["condition"], G)
            trueBody, G = parse_ast_node(node_dict["trueBody"], G)
            falseBody, G = (
                parse_ast_node(node_dict["falseBody"], G)
                if "falseBody" in node_dict
                else (None, G)
            )
            parsed_node = IfStatement(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                condition=condition,
                trueBody=trueBody,
                falseBody=falseBody,
                src=node_dict.get("src", ""),
                children=[],
            )

            G.add_edge(parsed_node.get_display_name(), condition.get_display_name())
            G.add_edge(condition.get_display_name(), trueBody.get_display_name())
            if falseBody:
                G.add_edge(condition.get_display_name(), falseBody.get_display_name())

        case "Return":
            expression, G = (
                parse_ast_node(node_dict["expression"], G)
                if "expression" in node_dict
                else (None, G)
            )
            parsed_node = ReturnValue(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                expression=expression,
                functionReturnParameters=node_dict.get("functionReturnParameters", 0),
                src=node_dict.get("src", ""),
                children=[],
            )
            if expression:
                G.add_edge(
                    parsed_node.get_display_name(), expression.get_display_name()
                )

        case "BinaryOperation":
            leftExpression, G = parse_ast_node(node_dict["leftExpression"], G)
            rightExpression, G = parse_ast_node(node_dict["rightExpression"], G)
            parsed_node = BinaryOperation(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                leftExpression=leftExpression,
                operator=node_dict.get("operator", ""),
                rightExpression=rightExpression,
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(
                parsed_node.get_display_name(), leftExpression.get_display_name()
            )
            G.add_edge(
                parsed_node.get_display_name(), rightExpression.get_display_name()
            )
        case "Literal":
            parsed_node = LiteralValue(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                hex_value=node_dict.get("hexValue", ""),
                is_constant=node_dict.get("isConstant", False),
                is_lvalue=node_dict.get("isLValue", False),
                is_pure=node_dict.get("isPure", False),
                kind=node_dict.get("kind", ""),
                lvalue_requested=node_dict.get("lValueRequested", False),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                value=node_dict.get("value", ""),
                subdenomination=node_dict.get("subdenomination", None),
                src=node_dict.get("src", ""),
                children=[],
            )

        case "VariableDeclarationStatement":
            declarations = []
            for decl in node_dict.get("declarations", []):
                if decl:
                    parsed_decl, G = parse_ast_node(decl, G)
                    declarations.append(parsed_decl)

            initialValue, G = (
                parse_ast_node(node_dict["initialValue"], G)
                if "initialValue" in node_dict
                else (None, G)
            )
            assignments = node_dict.get("assignments", [])
            parsed_node = VariableDeclarationStatement(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                declarations=declarations,
                initialValue=initialValue,
                assignments=assignments,
                src=node_dict.get("src", ""),
                children=[],
            )
            if initialValue:
                G.add_edge(
                    parsed_node.get_display_name(), initialValue.get_display_name()
                )
            for decl_node in declarations:
                G.add_edge(parsed_node.get_display_name(), decl_node.get_display_name())

        case "ElementaryTypeName":
            parsed_node = ElementaryTypeName(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                name=node_dict.get("name", ""),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=node_dict.get("src", ""),
                children=[],
            )
        case "ElementaryTypeNameExpression":
            typeName, G = parse_ast_node(node_dict["typeName"], G)
            argumentTypes = node_dict.get("argumentTypes", [])
            is_pure = node_dict.get("isPure", False)
            parsed_node = ElementaryTypeNameExpression(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                typeName=typeName,
                argumentTypes=argumentTypes,
                is_pure=is_pure,
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), typeName.get_display_name())

        case "RevertStatement":
            error_call, G = (
                parse_ast_node(node_dict["errorCall"], G)
                if "errorCall" in node_dict
                else (None, G)
            )
            parsed_node = RevertStatement(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                errorCall=error_call,
                src=node_dict.get("src", ""),
                children=[],
            )
            if error_call:
                G.add_edge(
                    parsed_node.get_display_name(), error_call.get_display_name()
                )
        case "MemberAccess":
            expression, G = parse_ast_node(node_dict["expression"], G)
            parsed_node = MemberAccess(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                expression=expression,
                memberName=node_dict.get("memberName", ""),
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), expression.get_display_name())

        case "ParameterList":
            parameters = []
            for param in node_dict.get("parameters", []):
                param_parsed, G = parse_ast_node(param, G)
                parameters.append(param_parsed)

            parsed_node = ParameterList(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                parameters=parameters,
                src=node_dict.get("src", ""),
                children=[],
            )
            for param in parameters:
                G.add_edge(parsed_node.get_display_name(), param.get_display_name())

        case "Conditional":
            condition, G = parse_ast_node(node_dict["condition"], G)
            true_expression, G = parse_ast_node(node_dict["trueExpression"], G)
            false_expression, G = parse_ast_node(node_dict["falseExpression"], G)
            parsed_node = Conditional(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                condition=condition,
                trueExpression=true_expression,
                falseExpression=false_expression,
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(parsed_node.get_display_name(), condition.get_display_name())
            G.add_edge(condition.get_display_name(), true_expression.get_display_name())
            G.add_edge(
                condition.get_display_name(), false_expression.get_display_name()
            )
        case "TupleExpression":
            components = []
            for comp in node_dict.get("components", []):
                if comp is not None:
                    parsed_comp, G = parse_ast_node(comp, G)
                    components.append(parsed_comp)
            parsed_node = TupleExpression(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                components=components,
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=node_dict.get("src", ""),
                children=[],
            )
            for component_node in components:
                G.add_edge(
                    parsed_node.get_display_name(), component_node.get_display_name()
                )
        case "IndexAccess":
            base_expression, G = parse_ast_node(node_dict["baseExpression"], G)

            index_expression = node_dict.get("indexExpression", None)
            if index_expression is not None:
                index_expression, G = parse_ast_node(index_expression, G)
            parsed_node = IndexAccess(
                node_id=node_dict.get("id", 0),
                node_type=node_dict.get("nodeType", ""),
                baseExpression=base_expression,
                indexExpression=index_expression,
                type_descriptions=node_dict.get("typeDescriptions", {}),
                src=node_dict.get("src", ""),
                children=[],
            )
            G.add_edge(
                parsed_node.get_display_name(), base_expression.get_display_name()
            )
            if index_expression is not None:
                G.add_edge(
                    parsed_node.get_display_name(), index_expression.get_display_name()
                )

        case "UnaryOperation":
            src = node_dict.get("src", "")
            is_constant = node_dict.get("isConstant", False)
            is_lvalue = node_dict.get("isLValue", False)
            is_pure = node_dict.get("isPure", False)
            lvalue_requested = node_dict.get("lValueRequested", False)
            operator = node_dict.get("operator", "")
            prefix = node_dict.get("prefix", False)
            type_descriptions = node_dict.get("typeDescriptions", {})

            # Parsing the subExpression, which can be of various types
            sub_expression_dict = node_dict.get("subExpression", {})
            sub_expression, G = (
                parse_ast_node(sub_expression_dict, G)
                if sub_expression_dict
                else (None, G)
            )

            parsed_node = UnaryOperation(
                node_id=node_id,
                node_type=node_type,
                is_constant=is_constant,
                is_lvalue=is_lvalue,
                is_pure=is_pure,
                lvalue_requested=lvalue_requested,
                type_descriptions=type_descriptions,
                operator=operator,
                prefix=prefix,
                src=src,
                subExpression=sub_expression,
                children=[],
            )

            # Adding edge to graph if subExpression exists
            if sub_expression:
                G.add_edge(
                    parsed_node.get_display_name(), sub_expression.get_display_name()
                )
        case "ForStatement":
            src = node_dict.get("src", "")

            init_expr_dict = node_dict.get("initializationExpression", {})
            initializationExpression, G = (
                parse_ast_node(init_expr_dict, G) if init_expr_dict else (None, G)
            )

            condition_dict = node_dict.get("condition", {})
            condition, G = (
                parse_ast_node(condition_dict, G) if condition_dict else (None, G)
            )

            loop_expr_dict = node_dict.get("loopExpression", {})
            loopExpression, G = (
                parse_ast_node(loop_expr_dict, G) if loop_expr_dict else (None, G)
            )

            body_dict = node_dict.get("body", {})
            body, G = parse_ast_node(body_dict, G) if body_dict else None

            parsed_node = ForStatement(
                initializationExpression=initializationExpression,
                condition=condition,
                loopExpression=loopExpression,
                body=body,
                node_id=node_id,
                src=src,
                node_type=node_type,
                children=[],
            )

            # Building relationships in the graph G if needed
            if initializationExpression:
                G.add_edge(
                    parsed_node.get_display_name(),
                    initializationExpression.get_display_name(),
                )
            if condition:
                G.add_edge(parsed_node.get_display_name(), condition.get_display_name())
            if loopExpression:
                G.add_edge(
                    parsed_node.get_display_name(), loopExpression.get_display_name()
                )
            if body:
                G.add_edge(parsed_node.get_display_name(), body.get_display_name())

        case "FunctionCallOptions":
            # Parsing FunctionCallOptions fields
            expression_dict = node_dict.get("expression", {})
            expression, G = (
                parse_ast_node(expression_dict, G, parent=node_id)
                if expression_dict
                else (None, G)
            )

            options = []
            for option_dict in node_dict.get("options", []):
                option, G = parse_ast_node(option_dict, G, parent=node_id)
                options.append(option)

            names = node_dict.get("names", [])
            type_descriptions = node_dict.get("typeDescriptions", {})
            node_id = node_dict.get("id", 0)
            src = node_dict.get("src", "")

            parsed_node = FunctionCallOptions(
                expression=expression,
                options=options,
                names=names,
                typeDescriptions=type_descriptions,
                src=src,
                node_id=node_id,
                node_type=node_type,
                children=[],
            )

            if parent:
                G.add_edge(parent, parsed_node.get_display_name())

            if expression:
                G.add_edge(
                    parsed_node.get_display_name(), expression.get_display_name()
                )
            for option in options:
                G.add_edge(parsed_node.get_display_name(), option.get_display_name())

        case _:
            # log("warning", f"Unsupported node type {node_type}")
            parsed_node = ASTNode(
                node_id=node_id,
                node_type=node_type,
                src=src,
                children=[],
            )
            # G.add_node(parsed_node.get_display_name())

    # Recursively process child node dictionaries
    for child_dict in child_dicts:
        child_node, G = parse_ast_node(child_dict, G, parent=parsed_node)
        if child_node:
            parsed_node.add_child(child_node)
            G.add_edge(parsed_node.get_display_name(), child_node.get_display_name())

    return parsed_node, G


def reduce_json(ast_json):
    # Maintain original file list array
    def extract_file_list_from_ast(ast_data):
        if "sources" in ast_data:
            return list(ast_data["sources"].keys())
        return []

    original_file_list = extract_file_list_from_ast(ast_json)

    # Function to remove keys in-place from a dictionary
    def remove_keys_in_place(dictionary):
        removal_list = [
            key
            for key in dictionary
            if any(substring in key for substring in settings.excluded_contracts)
        ]
        for key in removal_list:
            log("debug", f"Excluding {key}")
            del dictionary[key]

    for section in ["sources", "contracts"]:
        if section in ast_json:
            remove_keys_in_place(ast_json[section])

    return ast_json, original_file_list


def parse_solidity_ast(ast_json, G):
    """
    Parses the entire Solidity AST from the JSON representation.
    """
    root_nodes = []
    for key, node in ast_json.get("sources", {}).items():
        ast_node = node.get("AST", node.get("ast", {}))
        root_node, G = parse_ast_node(ast_node, G)

        if root_node:
            root_nodes.append(root_node)
    return root_nodes, G
