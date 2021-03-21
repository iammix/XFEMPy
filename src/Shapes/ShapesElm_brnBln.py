for iElBrn in range(len(vElBrn)):
    uElBrn = vElBrn[iElBrn]
    vBlRmp = mBlRmp[iElBrn, :]

    mElCrd = mNdCrd[mLNodS[uElBrn, :], :]

    ### Gauss shapes ###
    mGsShs = cGsEnr_omgShS(uElBrn)
    mGsDvS = cGsEnr_omgDvS(uElBrn)

    mGsCrd = mGsShS * mElCrd

    # import EnrFun_Brn
    mGFnVl, mGFnDv, mNdShf = EnrFun_Brn(mElCrd,mGsCrd,nEnFun_brn,vTpCrd,uTpAlf)
    #import ShapesEnr_WtBln
    nLNodE, mGsShE, mGsDvE = ShapesEnr_WtBln(mElCrd,mGsShS,mGsDvS,nEnFun_brn,mGFnVl,mGFnDv,mNdShf,vGBlVl,vGBlDv)

    #Clarify what the following code is doing
    cGsEnr_omgShE{uElBrn}(:,end+1:end+nLNodE) = mGsShE;
    cGsEnr_omgDvE{uElBrn}(:,end+1:end+nLNodE) = mGsDvE;