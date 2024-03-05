# Unchecked Chainlink Oracle Price
An intentionally vulnerable Foundry project.

```bash
tree
.
├── foundry.toml                                    # Contract's root
├── src/                                    
│   └── unchecked_chainlink_oracle_price.sol        # Vulnerable contract
```
## Usage

### Install dependencies
```bash
forge install smartcontractkit/chainlink --no-commit
```

### Build

```bash
forge build
```

### Test

```bash
forge test
```