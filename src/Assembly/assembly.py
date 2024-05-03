import numpy as np

# TODO Create assembly class with all the methods.
class YourClassName:
    def assemble_enr(self, nEnFun_hvi, nEnFun_brn, nLNodS, vElEnr, cLNodE, mNdCrd, vElPhz, nPhase, cDMatx, 
                     cGsEnr_omgDvS, cGsEnr_omgDvE, cGsEnr_omgWgt, nNdEnr, nDimes, with_Update, nGlDofS, 
                     wCkLod, nCrack, cCkCrd, mGsHvi_gamShp, vGsHvi_gamWgt, mCkLod, jEnJmp_brn, nLNodE_brn, 
                     mGlStf, nGlDof, wPrLod, mPrLod, wBdLod, vBdLod, mLNodS, nGDofS, mNDofE):
        # Enrichment control
        nLNodE_brn = nLNodS * nEnFun_brn
        nLNodE_hvi = nLNodS * nEnFun_hvi

        nEnJmp_brn = 1
        jEnJmp_brn = 1  # 1st enr. fun has jump (but, in general, can be a vector)

        # Determine enriched element topology
        AssembleEnr_Topology()

        # Determine standard shape functions for enriched elements
        AssembleEnr_ShapesStd()

        # Determine enriched shape functions for enriched elements
        AssembleEnr_ShapesEnr()

        # Ensure size compatibility of enr. shape functions and enr. nodes
        for i in vElEnr:
            if cLNodE[i].shape[1] != cGsEnr_omgShE[i].shape[1]:
                raise ValueError(f"Missmatch of size compatibility of enr. shape functions and enr. nodes. Element #{i}")

        # Get enr. dofs
        vNdEnr = list(range(1, nNdEnr + 1))

        nGDofE = nNdEnr * nDimes
        nGlDof = nGDofS + nGDofE

        mNDofE = np.zeros((nDimes, nNdEnr))
        mNDofE[:] = np.arange(nGDofS + 1, nGlDof + 1)

        if with_Update:  # saves mem.
            mNDofE = sparse(mNDofE)

        # Assemble Kg (enr.)
        mGlStf = MtxStiffEnr(nGlDof, mNdCrd, mLNodS, vElEnr, cLNodE, mNDofE, vElPhz, nPhase, cDMatx,
                             cGsEnr_omgDvS, cGsEnr_omgDvE, cGsEnr_omgWgt)

        # Assemble Fg (enr.)
        vGlFrc = np.zeros((nGlDof, 1))

        if wCkLod:
            vGlFrc_crk = \
                ForceEnr_BndCkHvi(nGlDof, nCrack, cCkCrd, mGsHvi_gamShp, vGsHvi_gamWgt, mCkLod) + \
                ForceEnr_BndCkBrn(nGlDof, nElEnr, jEnJmp_brn, nLNodS, nCrack, cCkCrd,
                                  nGsBrn_gam, mGsBrn_gamShp, vGsBrn_gamWgt, mCkLod)

            vGlFrc += vGlFrc_crk

        if wPrLod:
            vGlFrc += ForceEnr_Resid(nGlDof, mNdCrd, mLNodS, vElEnr, cLNodE, mNDofE, cGsEnr_omgDvS,
                                     cGsEnr_omgDvE, cGsEnr_omgWgt, mPrLod)

        if wBdLod:
            vGlFrc += ForceEnr_Body(nGlDof, mNdCrd, mLNodS, vElEnr, cLNodE, mNDofE, cGsEnr_omgDvS,
                                     cGsEnr_omgShE, cGsEnr_omgWgt, vBdLod)
