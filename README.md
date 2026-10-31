# createlab-mcp

Create Lab: Builds the rig, the holds and the clips for a new object.

4 tools replace 21. Each tool takes `action` and `args`, and calls the existing lab function
unchanged. Merged from: weaponlab-mcp (Gun Kit, Rig Lab, Motion Lab). Plan steps: 6 of
[the labs plan](https://github.com/hpdkhoa/poselab-mcp/blob/main/docs/MEANING_PLAN.md).

| Tool | Actions |
|---|---|
| `gunkit_build` | actions, action, draft, from_modellab, proxy, rig, build, export |
| `gunkit_check` | inspect, verify, cases |
| `rig_parts` | pieces, facts, align, part_line, fist |
| `motion` | roll_profile, roll, roll_set, track, render |

## Install

```bash
pip install "createlab-mcp @ git+https://github.com/hpdkhoa/createlab-mcp.git"
claude mcp add --scope user createlab -- createlab-mcp
```

## Test

```bash
pip install -e ".[test]" && pytest
```

MIT license.
