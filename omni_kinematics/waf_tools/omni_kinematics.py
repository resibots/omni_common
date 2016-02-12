#! /usr/bin/env python
# encoding: utf-8
# Federico Allocati - 2016

"""
Quick n dirty omni_kinematics detection
"""

from waflib.Configure import conf


def options(opt):
    opt.add_option('--omni_kinematics', type='string', help='path to omni_kinematics', dest='omni_kinematics')


@conf
def check_omni_kinematics(conf, **kw):
    includes_check = ['/usr/include', '/usr/local/include']

    if conf.options.resibots:
        includes_check = [conf.options.resibots + '/include'] + includes_check

    if conf.options.omni_kinematics:
        includes_check = [conf.options.omni_kinematics + '/include'] + includes_check

    conf.start_msg('Checking for omni_kinematics includes')
    try:
        res = conf.find_file('omni_kinematics/omnipointer.hpp', includes_check)
    except:
        res = False

    if res:
        conf.env.INCLUDES_OMNI_KINEMATICS = includes_check
        conf.end_msg('ok')
    else:
        if conf.options.omni_kinematics and conf.options.resibots:
            msg = 'not found in %s nor in %s' % (conf.options.omni_kinematics, conf.options.resibots)
        elif conf.options.omni_kinematics or conf.options.resibots:
            msg = 'not found in %s' % (conf.options.omni_kinematics if conf.options.omni_kinematics else conf.options.resibots)
        else:
            msg = 'not found, use --omni_kinematics=/path/to/omni_kinematics or --resibots=/path/to/resibots'

        if 'required' in kw and kw.get('required', False):
            conf.fatal(msg)
        else:
            conf.end_msg(msg, 'YELLOW')
