# Missing Reentracy Guard
An intentionally vulnerable Foundry project.

```bash
tree
.
├── foundry.toml                            # Contract's root
├── script/                                 
│   └── Attacker.sol                        # Attacker contract for the PoC
├── src/                                    
│   └── missing_reentrancy_guard.sol        # Vulnerable contract
├── test/                                   
│   └── poc.t.sol                           # Exploitation PoC
```
## Usage

### Build

```bash
forge build
```

### Test

```bash
forge test
```