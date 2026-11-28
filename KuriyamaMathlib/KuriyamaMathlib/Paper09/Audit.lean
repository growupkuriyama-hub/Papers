import KuriyamaMathlib.Families.BracketedDoubling
import KuriyamaMathlib.CFG.TypedRules
import KuriyamaMathlib.Distribution.DeletionCapture
import KuriyamaMathlib.Paper09

/-! Declaration-level audit of the 2026-11-28 manuscript.
TeX blob c6ef28a9a53a3459e14da2648ae860383e4936bf.
Only the following components are represented, not the entire paper. -/
#check KuriyamaMathlib.closure_product_subset
#check KuriyamaMathlib.rhsSet_closure_subset
#check KuriyamaMathlib.rhs_frames_insensitive
#check KuriyamaMathlib.typed_polar_galois
#check KuriyamaMathlib.typedClosure_idempotent
#check KuriyamaMathlib.typed_closed_iff_frames
#check KuriyamaMathlib.typed_subset_closure_iff
#check KuriyamaMathlib.typed_kernel_reduction_semigroup
#check KuriyamaMathlib.one_word_deletion_capture
#check KuriyamaMathlib.kernel_capture

#print axioms KuriyamaMathlib.rhs_frames_insensitive
#print axioms KuriyamaMathlib.typed_kernel_reduction_semigroup
#print axioms KuriyamaMathlib.one_word_deletion_capture
#print axioms KuriyamaMathlib.kernel_capture

#check KuriyamaMathlib.BracketedDoubling.cleanWord_length
#check KuriyamaMathlib.BracketedDoubling.unaryWord_length
#check KuriyamaMathlib.BracketedDoubling.deleted_iff_marked
#print axioms KuriyamaMathlib.BracketedDoubling.deleted_iff_marked
