import argparse
import tomllib
import yaml


def deep_merge(first_dict, second_dict):
    merged = first_dict.copy()

    for key, value in second_dict.items():
        if (isinstance(value, dict) and
            key in merged and
            isinstance(merged[key], dict)):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value

    return merged


def merge_toml_files(first_file, second_file):
    with open(first_file, "rb") as f:
        first_dict = tomllib.load(f)
    with open(second_file, "rb") as f:
        second_dict = tomllib.load(f)
    return deep_merge(first_dict, second_dict)


def save_as_yaml(config, output_file):
    with open(output_file, "w") as f:
        yaml.dump(config, f)


def parse_args():
    parser = argparse.ArgumentParser(description="Merge two TOML files")
    parser.add_argument("--first_file", type=str, help="First TOML file", required=True)
    parser.add_argument("--second_file", type=str, help="Second TOML file", required=True)
    parser.add_argument("--output_file", type=str, help="Output YAML file", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    config = merge_toml_files(args.first_file, args.second_file)
    save_as_yaml(config, args.output_file)