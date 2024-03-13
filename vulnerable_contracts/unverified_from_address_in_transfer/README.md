# Unverified from Address Usage in transferFrom
An intentionally vulnerable Foundry project.

```bash
tree
.
├── foundry.toml                                       # Contract's root
├── src/                                    
│   └── unverified_from_address_in_transfer.sol  # Vulnerable contract
```
## Usage

### Install dependencies
```bash
forge install OpenZeppelin/openzeppelin-contracts --no-git
```

### Build

```bash
forge build
```

### Test

```bash
forge test
```