import os
import sys
PROJECT_PATH = os.getcwd()
print(PROJECT_PATH)
SOURCE_PATH = os.path.join(PROJECT_PATH,"code")
sys.path.append(SOURCE_PATH)