#!/usr/bin/env python

TOP = '.'
APPNAME = 'WireCell'

def options(opt):
    opt.load('doxygen')
    opt.load('smplpkgs')
    opt.add_option('--build-debug', default='-O2',
                   help="Build with debug symbols")
    opt.add_option('--doxygen-tarball', default=None,
                   help="Build Doxygen documentation to a tarball")
    opt.add_option('--doxygen-install-path', default="",
                   help="Build Doxygen documentation to a tarball")

def configure(cfg):
    cfg.load('doxygen')
    cfg.load('smplpkgs')
    cfg.env.CXXFLAGS += [cfg.options.build_debug]

def build(bld):
    bld.load('smplpkgs')

    #subdirs = [str(sd.parent) for sd in bld.path.ant_glob('*/wscript_build')]
    subdirs = 'util iface gen rio riodata rootdict'.split()
    print subdirs

    bld.recurse(subdirs)
    if bld.env.DOXYGEN and bld.options.doxygen_tarball:
        bld(features="doxygen",
            doxyfile=bld.path.find_resource('Doxyfile'),
            install_path=bld.options.doxygen_install_path or bld.env.PREFIX + "/doc",
            doxy_tar = bld.options.doxygen_tarball)

