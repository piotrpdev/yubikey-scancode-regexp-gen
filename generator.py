import sys, pkgutil, importlib, re

# Add the scancodes folder to the path so we can import the modules
sys.path.append("./yubikey-manager/ykman/scancodes/")

# Iterate over all modules in the scancodes folder
for _, module_name, _ in pkgutil.iter_modules(["./yubikey-manager/ykman/scancodes/"]):
    module = importlib.import_module(module_name)

    # Newline and tab should not be used in the password, and \xa0 is a non-breaking space https://english.stackexchange.com/a/28476
    scancodes_without_control_characters = [ char for char in module.scancodes.keys() if char not in ["\n", "\t", "\xa0"] ]
    scancodes_combined = "".join(scancodes_without_control_characters)
    scancodes_combined_escaped = re.escape(scancodes_combined) # Escape special characters for RegExp
    scancodes_escape_forward_slash = [ char.replace("/", "\\/") for char in scancodes_combined_escaped ]
    scancodes_regexp = "/[" + "".join(scancodes_escape_forward_slash) + "]{1,38}$/"


    # Check if RegExp is valid (by Python's standards, you'd be surprised): https://stackoverflow.com/a/19631067/19020549
    is_valid_regexp = "Not Valid"
    try:
        re.compile(scancodes_regexp)
        is_valid_regexp = "Valid"
    except re.error:
        is_valid_regexp = "Not Valid"
    
    # Print with nice alignment
    print((f"'{module_name}' \t RegExp ({is_valid_regexp}): \t {scancodes_regexp}").expandtabs(10))
