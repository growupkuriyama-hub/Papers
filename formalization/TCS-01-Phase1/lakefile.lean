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

@[default_target]
lean_lib TCSPhase3CPathCongruence where

@[default_target]
lean_lib TCSPhase3CClarkEyraud where

@[default_target]
lean_lib TCSPhase3CMain where

@[default_target]
lean_lib TCSPhase4SSBNF where

@[default_target]
lean_lib TCSPhase4TypedLifting where

@[default_target]
lean_lib TCSPhase4Trimming where

@[default_target]
lean_lib TCSPhase4Thickness where

@[default_target]
lean_lib TCSPhase4IntrinsicGap where

@[default_target]
lean_lib TCSPhase4TrimmingLanguage where

@[default_target]
lean_lib TCSPhase4Main where

@[default_target]
lean_lib TCSPhase4FiniteRefinement where

@[default_target]
lean_lib TCSPhase4OperationalTrim where

@[default_target]
lean_lib TCSPhase5Factors where

@[default_target]
lean_lib TCSPhase5Derivations where

@[default_target]
lean_lib TCSPhase5Soundness where

@[default_target]
lean_lib TCSPhase5Consistency where

@[default_target]
lean_lib TCSPhase5Monotonicity where

@[default_target]
lean_lib TCSPhase5FactorsFinite where

@[default_target]
lean_lib TCSPhase5Grammar where

@[default_target]
lean_lib TCSPhase5FiniteDerivation where

@[default_target]
lean_lib TCSPhase5ConcreteGap where

@[default_target]
lean_lib TCSPhase5Main where

@[default_target]
lean_lib TCSPhase5BGeneralSSBNF where

@[default_target]
lean_lib TCSPhase5BTypedRefinement where

@[default_target]
lean_lib TCSPhase5BRetained where
