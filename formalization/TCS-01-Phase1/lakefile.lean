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

@[default_target]
lean_lib TCSPhase3Parser where

@[default_target]
lean_lib TCSPhase3Recognition where

@[default_target]
lean_lib TCSPhase3Congruence where

@[default_target]
lean_lib TCSPhase3Prefix where

@[default_target]
lean_lib TCSPhase3Main where

@[default_target]
lean_lib TCSPhase3Suffix where

@[default_target]
lean_lib TCSPhase3RecognitionConverse where

@[default_target]
lean_lib TCSPhase3Marker where

@[default_target]
lean_lib TCSPhase3RecognitionFull where

@[default_target]
lean_lib TCSPhase3Subtree where

@[default_target]
lean_lib TCSPhase3BMain where

@[default_target]
lean_lib TCSPhase3CAux where

@[default_target]
lean_lib TCSPhase3CSynchronization where
