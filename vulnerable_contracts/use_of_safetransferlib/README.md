# Use of SafeTransferLib
An intentionally vulnerable Foundry project.

```bash
tree
.
├── foundry.toml                                       # Contract's root
├── src/                                    
│   └── use_of_safetransferlib.sol  # Vulnerable contract
```
## Usage

### Install dependencies
```bash
forge install transmissions11/solmate --no-git
```

### Build

```bash
forge build
```

### Test

```bash
forge test
```