#! /usr/bin/env python
# encoding: utf-8
# JB Mouret - 2009
# Federico Allocati - 2016

"""
Quick n dirty eigen detection
"""

from waflib.Configure import conf


def options(opt):
    opt.add_option('--eigen', type='string', help='path to eigen', dest='eigen')


@conf
def check_omni_vrep(conf, **kw):
    includes_check = ['/usr/include/eigen3', '/usr/local/include/eigen3', '/usr/include', '/usr/local/include']

    if conf.options.resibots:
        includes_check = [conf.options.resibots + '/include'] + includes_check

    if conf.options.eigen:
        includes_check = [conf.options.eigen + '/include'] + includes_check

    conf.start_msg('Checking for Eigen includes')
    try:
        res = conf.find_file('Eigen/Core', includes_check)
    except:
        res = False

    if res:
        conf.env.INCLUDES_EIGEN = includes_check
        conf.end_msg('ok')
    else:
        if conf.options.eigen and conf.options.resibots:
            msg = 'not found in %s nor in %s' % (conf.options.eigen, conf.options.resibots)
        elif conf.options.eigen or conf.options.resibots:
            msg = 'not found in %s' % (conf.options.eigen if conf.options.eigen else conf.options.resibots)
        else:
            msg = 'not found, use --eigen=/path/to/eigen or --resibots=/path/to/resibots'

        if 'required' in kw and kw.get('required', False):
            conf.fatal(msg)
        else:
            conf.end_msg(msg, 'YELLOW')
