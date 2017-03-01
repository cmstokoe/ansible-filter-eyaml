# ansible-filter-eyaml
Ansible filter plugin to de-crypt eyaml encrypted variables

The typical approach to encrypting secrets with Ansible is to use ansible-vault or alternatively a third party encryption tool such as git-crypt. The problem with both of these methods is that they perform full file encryption thus turning your inventory and variable files into binary blobs. This makes it difficult to navigate and version your inventory facts within your chosen revision control system.

[Hiera-eyaml] ( https://github.com/TomPoulton/hiera-eyaml ) is a backend for the puppet hiera key/value store. It provides per-value / in-line encryption of sensitive data within yaml files. This jinja2 filter_plugin provides support for eyaml de-cryption in ansible.

Given the following yaml file:

```
---
plaintext_variable: “my variable”
secret_variable: >
    ENC[PKCS7,MIIBeQYJKoZIhvcNAQcDoIIBajCCAWYCAQAxggEhMIIBHQIBADAFMAACAQEw
    DQYJKoZIhvcNAQEBBQAEggEAlAsdarpE3+YcDCR2/VOcVo2URlmgTA0G1GKH
    idHXKry/mc7irPGErhnAO/T++MUQtyiNCEm0hEOx+y1fDUv0v3NNzXvhoDwl
    ug0xJEOVToE5PR5aPXnmj8QtCrwRbbkiq4PXkxPsznhVn5k70wlI3C9SbciF
    xV6pjHHOzYoC/E9cdw9CvtzoTmKPJzAVhIAwC7g7eqvOW41JySO3AEwjj49I
    e6V9X0OtmEAYxXjjbtiq2LRqzQ3QP3rHbiGeHjNoq0S+6umuoMZblDvGnGQu
    0Vd61IS+IcsLPv0/EMFnzme2D8HXc+C5hD31AzfMWzOT8c85iRUlohyXTokS
    XRZxbzA8BgkqhkiG9w0BBwEwHQYJYIZIAWUDBAEqBBC4VCBEfwwPn33Rbd0t
```

The in-line encrypted variable can be referenced and automaticly de-crypted within your ansible plays/roles using the following Jinja2 instantiation {{ secret_variable | eyaml }}.

Obvioulsy it depends on a working installation of hiera-eyaml being avaialble.

To produce encrypted variables for inclusion in your inventory you can use the eyaml command line tool:

```
eyaml encrypt -s "plain text variable"
```

Author
------
- [Chris Stokoe](http://github.com/cmstokoe)
