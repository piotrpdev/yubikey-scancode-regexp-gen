# YubiKey Scancode RegExp Generator

Converts the [`yubikey-manager`](https://github.com/Yubico/yubikey-manager) scancodes to valid<sup>\[1\]</sup> regular expressions.

## Usage

The following script will generate regular expressions for all of the available scancodes in `./yubikey-manager/ykman/scancodes/` and write them to `scancodes_regexp_file.txt`.

```bash
git clone --recurse-submodules https://github.com/piotrpdev/yubikey-scancode-regexp-gen.git && \
cd yubikey-scancode-regexp-gen && \
python3 generator.py
```

### Example console output

> [!WARNING]
> Don't use the output below, the generated file wil include important Unicode characters. The output is also generated based on the current version of the [`yubikey-manager`](https://github.com/Yubico/yubikey-manager) scancodes, which can change.

```bash
$ python3 generator.py 
'bepo'     RegExp (Valid):     /[\ !"\#\$%'\(\)\*\+,\-\.\/0123456789:;=\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ`abcdefghijklmnopqrstuvwxyz«°»ÀÇÈÉÊàçèéê]{1,38}$/
'de'       RegExp (Valid):     /[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"\#\$%\&'\(\)\*\+,\-\.\/:;<=>\?\^_\ `§´ÄÖÜßäöü]{1,38}$/
'fr'       RegExp (Valid):     /[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\ !"\$%\&'\(\)\*\+,\-\.\/:;<=_£§°²µàçèéù]{1,38}$/
'it'       RegExp (Valid):     /[\ !"\#\$%\&'\(\)\*\+,\-\.\/0123456789:;<=>\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\\^_`abcdefghijklmnopqrstuvwxyz\|£§°çèéàìòù]{1,38}$/
'modhex'   RegExp (Valid):     /[bcdefghijklnrtuvBCDEFGHIJKLNRTUV]{1,38}$/
'norman'   RegExp (Valid):     /[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"\#\$%\&'`\(\)\*\+,\-\.\/:;<=>\?@\[\\\]\^_\{\}\|\~\ ]{1,38}$/
'uk'       RegExp (Valid):     /[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@£\$%\&'`\(\)\*\+,\-\.\/:;<=>\?"\[\#\]\^_\{\}\~¬\ ]{1,38}$/
'us'       RegExp (Valid):     /[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"\#\$%\&'`\(\)\*\+,\-\.\/:;<=>\?@\[\\\]\^_\{\}\|\~\ ]{1,38}$/
```

## Notes

In the future, using [Matthew Barnett’s excellent `regex` module](https://pypi.org/project/regex/) instead of the built-in `re` module might be a better choice. The `regex` module is a drop-in replacement, provides full support for [Perl-style regular expressions (PCRE)](https://www.pcre.org/), and has much better Unicode support<sup>[\[2\]][2]</sup>.

Considering a YubiKey is usually configured using `yubikey-manager` ([which is written in Python](https://github.com/Yubico/yubikey-manager/blob/51a7ae438c923189788a1e31d3de18d452131942/README.adoc?plain=1#L7)) using the built-in `re` module be fine.

As of me writing this (November 11, 2023), both modules generated the same output.

## Footnotes

\[1\]: Valid by Python's standards, see relevant comments in [`generator.py`](generator.py).

\[2\]: <https://stackoverflow.com/questions/7063420/perl-compatible-regular-expression-pcre-in-python>

[2]: https://stackoverflow.com/questions/7063420/perl-compatible-regular-expression-pcre-in-python
