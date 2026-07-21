import sys
from pathlib import Path

#adding the project root to python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.main import main

if __name__ == "__main__":
    print("Enterprise Workspace Scaffolding")
    
    main()
    
    print("Application run complete. Check logs for details.")