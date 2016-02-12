#! /usr/bin/env python
# encoding: utf-8
# Federico Allocati - 2016

"""
Quick n dirty omni_kinematics detection
"""

import os
from waflib.Configure import conf


def options(opt):
    opt.add_option('--omni_kinematics', type='string', help='path to omni_kinematics', dest='omni_kinematics')


@conf
def check_omni_kinematics(conf, **kw):
    includes_check = ['/usr/include', '/usr/local/include']
    resibots_dir = conf.options.resibots if hasattr(conf.options, 'resibots') and conf.options.resibots else None

    if resibots_dir:
        includes_check = [resibots_dir + '/include'] + includes_check

    if conf.options.omni_kinematics:
        includes_check = [conf.options.omni_kinematics + '/include'] + includes_check

    conf.start_msg('Checking for omni_kinematics includes')
    try:
        res = conf.find_file('omni_kinematics/omnipointer.hpp', includes_check)
    except:
        res = False

    if res:
        conf.env.INCLUDES_OMNI_KINEMATICS = [os.path.expanduser(include) for include in includes_check]
        conf.env.DEFINES_OMNI_KINEMATICS = ['USE_OMNI_KINEMATICS']
        conf.end_msg('ok')
    else:
        if conf.options.omni_kinematics and resibots_dir:
            msg = 'not found in %s nor in %s' % (conf.options.omni_kinematics, resibots_dir)
        elif conf.options.omni_kinematics or resibots_dir:
            msg = 'not found in %s' % (conf.options.omni_kinematics if conf.options.omni_kinematics else resibots_dir)
        else:
            msg = 'not found, use --omni_kinematics=/path/to/omni_kinematics or --resibots=/path/to/resibots'

        if 'required' in kw and kw.get('required', False):
            conf.fatal(msg)
        else:
            conf.end_msg(msg, 'YELLOW')
