# Known Git Issues

## Purpose
Document common issues and their resolutions.

### Examples
1. **Issue**: Large Files in Repository
   - **Resolution**: Use Git LFS (Large File Storage):
     ```bash
     git lfs install
     git lfs track "*.largefile"
     ```

2. **Issue**: Slow Repository Cloning
   - **Resolution**: Use a shallow clone:
     ```bash
     git clone --depth 1 <repository-url>
     ```

