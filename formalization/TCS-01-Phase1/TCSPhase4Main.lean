import TCSPhase4IntrinsicGap
import TCSPhase4TrimmingLanguage
import TCSPhase4FiniteRefinement
import TCSPhase4OperationalTrim

/-!
Theorem-audit entry point for the presentation-independent Corollary 6.4.
All classes and relations below are defined by concrete finite grammars
and independent derivation trees; old Phase 1–3C statements are unchanged.
-/

#print axioms TCSPhase4.nonempty_start_has_root
#print axioms TCSPhase4.typed_lifting
#print axioms TCSPhase4.trimmed_lifting
#print axioms TCSPhase4.trimmed_grammar_language_eq
#print axioms TCSPhase4.shortestTypedLength_spec
#print axioms TCSPhase4.shortestTypedLength_le
#print axioms TCSPhase4.shortest_le_typedThickness
#print axioms TCSPhase4.intrinsic_typed_thickness_lower_bound_all
#print axioms TCSPhase4.intrinsic_typed_thickness_lower_bound

#print axioms TCSPhase4.shortest_length_characterization
#print axioms TCSPhase4.finite_trimmed_terminal_iff
#print axioms TCSPhase4.finite_trimmed_binary_iff
#print axioms TCSPhase4.finite_trimmed_start_iff
#print axioms TCSPhase4.finite_trimmed_complete
#print axioms TCSPhase4.finite_trimmed_sound
#print axioms TCSPhase4.finite_trimmed_productive_iff_retained
#print axioms TCSPhase4.finite_trimmed_lifting
#print axioms TCSPhase4.finite_trimmed_grammar_language_eq
#print axioms TCSPhase4.finite_trimmed_shortest_length
#print axioms TCSPhase4.operational_retained_iff
#print axioms TCSPhase4.finite_operational_terminal_iff
#print axioms TCSPhase4.finite_operational_binary_iff
