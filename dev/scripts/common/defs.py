#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file provides defines

# Define codec
CODEC = 'utf8'

# Default paths where dictionaries are located
# Japhug lexicon
DICT_JAP = "../../dict/japhug/toolbox/Dictionary.txt"
# Khaling lexicon
DICT_KLR = "../../dict/khaling/toolbox/Dictionary.txt"
# Na lexicon
DICT_NA = "../../dict/na/lexique_na_2013sq_POUR_TRANSFERT.xls"
# Test files
TEST_JAP1 = "./test/japhug/input/japhug1.txt"
TEST_JAP2 = "./test/japhug/input/japhug2.txt"
TEST_KLR1 = "./test/khaling/input/khaling1.txt"
TEST_KLR2 = "./test/khaling/input/khaling2.txt"
TEST_NA1 = "./test/na/na1.xls"
# Lexique Pro databases
LP_DB_JAP = "../../dict/japhug/lexique_pro/japhug.db"
LP_DB_KLR = "../../dict/khaling/lexique_pro/khaling.db"
# Toolbox hierarchical structures
TB_STRUCT_JAP = "../../dict/japhug/toolbox/Settings/MDF_AltH.typ"
TB_STRUCT_KLR = "../../dict/khaling/toolbox/Settings/MDF_AltH.typ"

# Define grammars
GRAMMAR_JAP1 = r"""
    lxGroup: {<lx><wav>*<wav8>*<ng>*<seGroup|psGroup>+<cf>}
    seGroup: {<se><psGroup>+}
    psGroup: {<ps><ng>*<msGroup|geGroup>+<hbf>?<cf>?}
    msGroup: {<mr>+<geGroup>+}
    geGroup: {<dv|gv|de|ge|dn|gn|dr|gr>*<uv|ue|un|ur>*<hbf>?<xvGroup>+}
    xvGroup: {<xv><xe|xn|xr>*}
    """
GRAMMAR_JAP2 = r"""
    lxGroup: {<lx><wav>*<wav8>*<ng>*<seGroup|psGroup>+<cf>}
    seGroup: {<se><psGroup>+}
    psGroup: {<ps><msGroup|geGroup>+<cf>?}
    msGroup: {<mr>+<geGroup>+}
    geGroup: {<dv|gv|de|ge|dn|gn|dr|gr>*<uv|ue|un|ur>*<hbf>?<xvGroup>+}
    xvGroup: {<xv><xe|xn|xr>*}
    """
GRAMMAR_KLR1 = r"""
    lxGroup: {<lx><wav>*<wav8>*<ng>*<seGroup|psGroup>+<cf>}
    seGroup: {<se><psGroup>+}
    psGroup: {<ps><ng>*<msGroup|geGroup>+<hbf>?<cf>?}
    msGroup: {<mr>+<geGroup>+}
    geGroup: {<dv|gv|de|ge|dn|gn|dr|gr>*<uv|ue|un|ur>*<hbf>?<xvGroup>+}
    xvGroup: {<xv|xn><xn|xe|xr>*}
    """
GRAMMAR_KLR2 = r"""
    lxGroup: {<lx><wav>*<wav8>*<ng>*<seGroup|psGroup>+<cf>}
    seGroup: {<se><psGroup>+}
    psGroup: {<ps><ng>*<msGroup|geGroup>+<hbf>?<cf>?<_1s|_1p|_2s|_2p|_3s|_3p|_1d|_1e|_4s|_3d>*}
    msGroup: {<mr>+<geGroup>+}
    geGroup: {<dv|gv|de|ge|dn|gn|dr|gr>*<uv|ue|un|ur>*<hbf>?<xvGroup>+}
    xvGroup: {<xv|xn><xn|xe|xr>*}
    """
GRAMMAR_NA = r"""
    lxGroup: {<lx><sf>*<hm><ph><bw><etGroup><psGroup><seGroup>*}
    etGroup: {<et><ec>}
    psGroup: {<ps><sn><cf>*<sd>*<nt>*<np>*<nd><so><vaGroup>*<msGroup|geGroup|rfGroup>+}
    vaGroup: {<va><vf>*}
    msGroup: {<ms>*<geGroup>+}
    geGroup: {<dv|gv|de|ge|dn|gn|dr|gr|df|gf>*<xvGroup>+}
    xvGroup: {<xv><xf><xc>?}
    rfGroup: {<rf><xvGroup>+}
    seGroup: {<se><sf>*<hm><ph><bw><etGroup><psGroup>}
    """
