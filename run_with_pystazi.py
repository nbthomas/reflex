import sys
import os
import builtins

# NOTE: This is a hack to import the pystazi module. Ideally this is
#       able to be removed in the future, when the module can be installed
#       and imported as a package.
#       SIDE-NOTE: Once the module is installed, I am unsure how the user will
#                  use the script portion of our project.
sys.path.append("../") # This enables the import of the pystazi module
from pystazi_package.pystazi import dependency_tracker, test_selector

dependency_tracker.start_tracking()
# builtins.__import__ =  dependency_tracker.track_import
# run pytest .\tests
os.system("pytest .\\tests")

# modified_files = test_selector.load_hashes_state()

modified_files = test_selector.get_modified_files(".", "hashing_state.json")
print("Modified files: ", modified_files)

dependency_map = test_selector.load_dependency_map()
print("Dependency map: ", dependency_map)

selected_tests = test_selector.select_tests(modified_files, dependency_map)
print("Selected tests: ", selected_tests)

print("\n")

# Run the selected tests
# for test in selected_tests:
#     os.system("pytest " + test)
