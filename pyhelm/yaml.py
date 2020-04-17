import ruamel.yaml

yaml = ruamel.yaml.YAML(typ="safe", pure=True)
yaml.default_flow_style = False
yaml.version = (1, 1)
yaml.preserve_quotes = True
yaml.allow_duplicate_keys = True
