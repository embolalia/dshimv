# `dshimv`

`dshimv` is intended to give software maintainers a simpler option for
achieving backward-compatibility with SysV Init (and other init systems that
support simmilar init scripts, like Upstart). By adding a few lines to a
systemd service unit, it can be dropped in and work exactly as a regular init
script would.

## Principal

The elegance (and part of the pain) of old-school init scripts is that they are
simply executable files. In practice, they make use of `#!`; a magic
pair of bytes that tells the OS to execute them a bit differently. Whatever
comes between `#!` and `\n` is treated as a command, and is given the name of
the file you executed (and any arguments thereto) as arguments. With init
scripts, this is usually a shell.

`dshimv` is a program that takes a systemd service unit file and an action. It
parses the file and gets the command associated with that action, and runs it.
So if you take a systemd service unit file, and throw a `#!` at the top
pointing to `dshimv`, you now have an executable that acts just like a SysV
Init script.

## Limitations

Obviously, anything that SysV Init isn't able to handle, `dshimv` can't do
either. Additionally, `dshimv` currently uses Python's `ConfigParser` to parse
files, and that may or may not have some differences from how systemd parses in
some edge cases. For simplicity, `dshimv` also uses simple shell execution of
the specified commands, rather than the limited subset that systemd does. This
means `dshimv` is a bit more permissive about what's valid than systemd.
Finally, there is almost certainly a performance detriment to using `dshimv`
over native scripts, though only when starting/stopping/etc. a service.

