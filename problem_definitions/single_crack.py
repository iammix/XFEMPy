import os
import time
import math
import numpy as np
from utilities import read_mesh_file


class Single_Crack():
    def __init__(self):
        self.job_subID = 'single_crack'
        nStep = 0
        self.with_meshread = False
        self.with_layered = False
        self._check_meshread_layerd()
        self.mesh_ElemType = 'Q4'
        self.mesh_EnriSize = 'big'
        self.kind_LawDir = 'energy'
        self.kind_LawCrt = 'energy'
        self.kind_CrwCrt = 'all'
        if self.kind_CrwCrt == 'custom':
            with_CrwCrt_inf = 0.5
        with_Update = True
        with_RdoStd = True
        with_MapTyp = True
        with_AdpEnr = False

        # Energy minimization
        with_GLwInc = False
        with_GLwDir = False
        with_DirAvg = False

        if with_GLwDir:
            nInter_dir = 5
            dBetaTol_iterDir = 0.01 * math.pi / 180
            dBetaMin_iterDir = 0.01 * math.pi / 180
        if with_GLwInc:
            dBetaMin_iterDir = 5.0 * math.pi / 180 * 0.0

        with_RfnInc = False
        with_RfnXrs = False

        if with_RfnInc or with_RfnXrs:
            nRefine_inc = 1
            nRefine_xrs = 3

            dBetaMin_mshFine = (5.0 * math.pi / 180) * 0.0
            dBetaMax_mshCors = (1.0 * math.pi / 180) * 0.0

        with_BndXrs = True
        if with_BndXrs:
            with_BndXrs_refine = True
            with_BndXrs_freeze = True

        with_JIntegral = False
        with_Roughness = False

        save_CracksEnd = False
        save_CracksAll = False
        save_StressAll = False
        save_DisplcAll = False
        save_StateVerb = False
        save_Roughness = False

        # Plotting (during Analysis)
        plot_mesh = True
        plot_domain = False
        plot_cracks = True
        plot_enriched = True
        plot_displace = False
        plot_deformed = False
        plot_VonMises = True
        plot_vmsContr = False

        # Plotting (final)
        plot_potential = False
        plot_dissipGlb = False
        plot_roughness = False

        # Generate Videos
        mov_cracks = False
        mov_vonmises = False
        mov_deformed = False


        # Material Data
        self.problemType = 'PlaneStress'
        self.lengthUnits = 'mm'
        self.nPhase = 1
        self.E = 1000
        self.v = 0.3
        self.k_crt = 1

        # Mesh
        if self.with_meshread:

    def _unit_conversion(self):
        if self.lengthUnits == '\mum':
            self.k_crt = self.k_crt * 1e3
        elif self.lengthUnits == 'mm':
            self.k_crt = self.k_crt * math.sqrt(1e3)
        elif self.lengthUnits == 'm':
            pass
        else:
            self._check_units()

    # Check Methods
    def _check_units(self):
        if self.lengthUnits not in ['\mum', 'mm', 'm']:
            raise ValueError("The lengthUnits must ne \mum, mm, m")

    def _check_problemType(self):
        if self.problemType not in ['PlaneStress', 'PlaneStrain']:
            raise ValueError("The problemType must be PlaneStress, PlaneStrain")

    def _check_kind_CrwCrt(self):
        if self.kind_CrwCrt not in ['maxinum', 'symmetric', 'critical', 'all', 'custom']:
            raise ValueError("The kind_CrwCrt  must be maxinum, symmetric, critical, all, custom")

    def _check_kind_LawCrt(self):
        if self.kind_LawCrt not in ['tension', 'energy', 'J-int', 'eliptic', 'Hayashi', 'Nuismer']:
            raise ValueError("The kind_LawCrt must be tension, energy, J-int, eliptic, Hayashi, Nuismer")

    def _check_kind_LawDir(self):
        if self.kind_LawDir is not 'maxhoop' or 'energy' or 'symmetry':
            raise ValueError("The kind_LawDir must be maxhoop, energy or symmetry")

    def _check_ElemType(self):
        if self.mesh_ElemType is not 'Q4' or 'T3':
            raise ValueError("The mesh_ElemType must be Q4 or T3")

    def _check_EnriSize(self):
        if self.mesh_EnriSize is not 'small' or 'normal' or 'big':
            raise ValueError("The mesh_EnriSize must be small, normal or big")

    def _check_meshread_layerd(self):
        if self.with_layered == 1:
            self.with_meshread = 0
