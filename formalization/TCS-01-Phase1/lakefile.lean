import Lake
open Lake DSL

package «TCSPhase1» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.24.0"

@[default_target]
lean_lib TCSPhase1 where

@[default_target]
lean_lib TCSPhase2 where

@[default_target]
lean_lib TCSPhase2Bridge where
