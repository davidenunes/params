import os
import configobj


def write_config_files(param_space, output_path="params", file_prefix="params", conf_id_header="conf_id"):
    """ Writes one configobj file for each parameter configuration in the parameter space
    to a given path

    Args:
        param_space: a `ParameterSpace` instance
        output_path: the path where the configuration files are to be created
        file_prefix : a prefix for the params created to be followed by their id (enumeration)
        (e.g. if default is kept, the prefix is params and the files are written as "params_0.conf")
    """

    param_grid = param_space.param_grid()
    conf_id = 0
    for current_config in param_grid:
        current_config[conf_id_header] = conf_id
        conf_file = "{prefix}_{id}.conf".format(prefix=file_prefix, id=conf_id)
        conf_file = os.path.join(output_path, conf_file)
        conf_obj = configobj.ConfigObj()
        conf_obj.filename = conf_file
        conf_obj.update(current_config)
        conf_obj.write()
        conf_id += 1
