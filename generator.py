import sys, pkgutil, importlib, re, datetime, platform

# Add the scancodes folder to the path so we can import the modules
sys.path.append("./yubikey-manager/ykman/scancodes/")

scancodes_regexp_list = []

#Iterate over all modules in the scancodes folder
for _, module_name, _ in pkgutil.iter_modules(["./yubikey-manager/ykman/scancodes/"]):
    module = importlib.import_module(module_name)

    # Newline and tab should not be used in the password
    scancodes_without_control_characters = [ char for char in module.scancodes.keys() if char not in ["\n", "\t"] ]
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
    
    # Nice alignment
    scancodes_regexp_list.append((f"'{module_name}' \t RegExp ({is_valid_regexp}): \t {scancodes_regexp}").expandtabs(10))

# ? User's console might not support UTF-8 and converting the '\x??' escape
# ? sequences to UTF-8 is annoying, so we'll just write to a UTF-8 file
with open("scancodes_regexp_file.txt", "w", encoding="utf-8") as scancodes_regexp_file:
    # Write some info about the environment
    scancodes_regexp_file.write(("Platform: \t " + platform.system() + " " + platform.release() + "\n").expandtabs(30))
    scancodes_regexp_file.write(("Python: \t " + sys.version + "\n").expandtabs(30))
    scancodes_regexp_file.write(("Generated at: \t " + datetime.datetime.now().astimezone().isoformat() + "\n\n").expandtabs(30))

    for scancodes_regexp in scancodes_regexp_list:
        print(scancodes_regexp)
        scancodes_regexp_file.write(scancodes_regexp + "\n")

    scancodes_regexp_file.close()
