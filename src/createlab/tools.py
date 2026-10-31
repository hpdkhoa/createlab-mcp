"""The 4 tools of Create Lab: tool -> (summary, [(module, function, action)]).

Each action calls the existing lab function unchanged. 21 former tools.
"""

TOOLS = {'gunkit_build': ('Gun Kit: actions, one action, draft, from Model Lab, proxy, rig, build, export.',
                  [('weaponlab.server', 'gunkit_actions', 'actions'),
                   ('weaponlab.server', 'gunkit_action', 'action'),
                   ('weaponlab.server', 'gunkit_draft', 'draft'),
                   ('weaponlab.server', 'gunkit_from_modellab', 'from_modellab'),
                   ('weaponlab.server', 'gunkit_proxy', 'proxy'),
                   ('weaponlab.server', 'gunkit_rig', 'rig'),
                   ('weaponlab.server', 'gunkit_build', 'build'),
                   ('weaponlab.server', 'gunkit_export', 'export')]),
 'gunkit_check': ('Gun Kit checks: inspect, verify, cases.',
                  [('weaponlab.server', 'gunkit_inspect', 'inspect'),
                   ('weaponlab.server', 'gunkit_verify', 'verify'),
                   ('weaponlab.server', 'gunkit_cases', 'cases')]),
 'rig_parts': ('Rig Lab: pieces, facts, align, part line, fist.',
               [('weaponlab.server', 'rig_pieces', 'pieces'),
                ('weaponlab.server', 'rig_facts', 'facts'),
                ('weaponlab.server', 'rig_align', 'align'),
                ('weaponlab.server', 'rig_part_line', 'part_line'),
                ('weaponlab.server', 'rig_fist', 'fist')]),
 'motion': ('Motion Lab: roll profile, roll, roll set, track, render.',
            [('weaponlab.server', 'motion_roll_profile', 'roll_profile'),
             ('weaponlab.server', 'motion_roll', 'roll'),
             ('weaponlab.server', 'motion_roll_set', 'roll_set'),
             ('weaponlab.server', 'motion_track', 'track'),
             ('weaponlab.server', 'motion_render', 'render')])}
