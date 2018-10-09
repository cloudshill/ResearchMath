################################################################################
# LIBRARIES USED
################################################################################
import resource                 # Used for Memory

################################################################################
# FUNCTIONS
################################################################################
#-------------------------------------------------------------------------------
def HowsMyMemory():
    import datetime, resource
    print("TIME:    "+str(datetime.datetime.now()))
    print('Memory usage: %s (kb)' % resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
#-------------------------------------------------------------------------------
def EndCode():
    import time
    print('Code Ended at '+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
#-------------------------------------------------------------------------------
def Scatter(x,y,z,c='b',marker='o',depthshade=True,xlabel='',ylabel='',zlabel=''):
    import numpy    as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z,c=c,marker=marker,depthshade=depthshade)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
#-------------------------------------------------------------------------------
def ViewAvailableFonts():
    import matplotlib.font_manager
    list = matplotlib.font_manager.get_fontconfig_fonts()
    names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in list]
    print(names)
    # ['Liberation Sans', 'DejaVu Sans', 'mry_KacstQurn', 'Lato', 'Lato', 'Tlwg Mono', 'Tlwg Typewriter', 'Umpush', 'FreeMono', 'Umpush', 'STIXVariants', 'NanumGothic', 'STIXSizeFourSym', 'KacstTitleL', 'Norasi', 'DejaVu Sans', 'Loma', 'Liberation Sans Narrow', 'Liberation Sans Narrow', 'Asgalt', 'KacstBook', 'DejaVu Sans', 'Norasi', 'DejaVu Serif', 'STIX', 'Sawasdee', 'Ubuntu Condensed', 'FreeSerif', 'Liberation Sans', 'KacstOffice', 'Umpush', 'STIXGeneral', 'FreeSans', 'Sawasdee', 'Umpush', 'Tlwg Typo', 'TakaoPGothic', 'FreeSans', 'Padauk Book', 'Minion Pro', 'Symbola', 'Waree', 'KacstOne', 'Lato', 'Lato', 'Tlwg Typo', 'Laksaman', 'STIXSizeThreeSym', 'DejaVu Sans', 'KacstArt', 'Liberation Mono', 'KacstPen', 'DejaVu Serif', 'Liberation Serif', 'Liberation Mono', 'Khmer OS System', 'Ubuntu', 'KacstQurn', 'STIXIntegralsSm', 'Ubuntu', 'Ubuntu Mono', 'Kinnari', 'STIXSizeOneSym', 'Tlwg Mono', 'Ubuntu Mono', 'NanumMyeongjo', 'STIXGeneral', 'KacstDecorative', 'Loma', 'Garuda', 'FreeSerif', 'Padauk', 'STIXSizeFiveSym', 'Ubuntu', 'Tlwg Typewriter', 'DejaVu Serif', 'Ubuntu', 'FreeMono', 'DejaVu Sans', 'Liberation Sans', 'Ubuntu', 'Norasi', 'STIXIntegralsUpSm', 'Laksaman', 'Lato', 'Liberation Serif', 'Lato', 'Warnock Pro', 'DejaVu Sans', 'DejaVu Sans Mono', 'TakaoPGothic', 'Waree', 'Liberation Sans', 'DejaVu Sans', 'STIXGeneral', 'Tlwg Typist', 'Norasi', 'STIXNonUnicode', 'Kinnari', 'Sylfaen', 'Khmer OS', 'Liberation Sans Narrow', 'Sawasdee', 'FreeSerif', 'Purisa', 'STIX Math', 'Liberation Mono', 'DejaVu Sans Mono', 'STIXIntegralsUpD', 'FreeSerif', 'Loma', 'Tlwg Typist', 'Lato', 'Tibetan Machine Uni', 'OpenSymbol', 'Liberation Serif', 'STIXSizeTwoSym', 'Sawasdee', 'Umpush', 'Waree', 'DejaVu Sans Mono', 'Lato', 'Waree', 'STIXVariants', 'Ubuntu', 'STIXSizeFourSym', 'Tlwg Mono', 'Lato', 'Ubuntu Mono', 'NanumMyeongjo', 'STIXNonUnicode', 'DejaVu Serif', 'Loma', 'Lato', 'Lato', 'DejaVu Sans', 'KacstDigital', 'KacstTitle', 'Liberation Sans Narrow', 'Garuda', 'Garuda', 'DejaVu Serif', 'NanumBarunGothic', 'STIX', 'Lato', 'Purisa', 'Lato', 'DejaVu Serif', 'DejaVu Sans', 'LKLUG', 'Tlwg Typo', 'Lato', 'KacstNaskh', 'STIXSizeThreeSym', 'KacstLetter', 'Tlwg Typist', 'Tlwg Typewriter', 'Ubuntu Mono', 'Kinnari', 'Norasi', 'Lato', 'STIXIntegralsUp', 'KacstOne', 'DejaVu Serif', 'Tlwg Typewriter', 'Bebas Neue', 'STIXIntegralsD', 'Kinnari', 'Purisa', 'Norasi', 'KacstFarsi', 'Laksaman', 'STIXIntegralsSm', 'STIX', 'DejaVu Serif', 'STIXGeneral', 'NanumBarunGothic', 'Abyssinica SIL', 'Lohit Punjabi', 'STIX', 'Lato', 'Kinnari', 'Liberation Serif', 'Padauk Book', 'Umpush', 'DejaVu Sans Mono', 'FreeMono', 'Phetsarath OT', 'STIXNonUnicode', 'Liberation Mono', 'Tlwg Mono', 'STIXIntegralsD', 'Saab', 'Tlwg Typo', 'FreeSans', 'FreeMono', 'NanumGothic', 'Tlwg Typist', 'Lato', 'Laksaman', 'STIXIntegralsUp', 'STIXSizeTwoSym', 'FreeSans', 'Ubuntu', 'KacstScreen', 'STIXIntegralsUpD', 'Kinnari', 'STIXSizeOneSym', 'STIXNonUnicode', 'KacstPoster', 'Padauk', 'Garuda', 'Purisa', 'Ubuntu', 'Lato', 'STIXIntegralsUpSm']
#-------------------------------------------------------------------------------
def ScatterWithHist(x, y, scatterstyle='bo', bin_no = None, cx = 'red', cy = 'cyan',alphaVal=0.5):
    # Description:
    #   This plots your xy plots but also puts in the histogram distribution of
    #   the x values on the x-axis and the histogram distribution of the y values
    #   on the y-axis.
    #   This was originally suggested by Dr. Gari Clifford as a sanity check to
    #   make sure that your data was properly distributed.
    import numpy    as np
    import matplotlib.pyplot as plt
    fig, ax1 = plt.subplots()

    ax1.plot(x,y,scatterstyle)
    ax2 = ax1.twinx()
    ax2.hist(x,bins=bin_no,color=cx,orientation='vertical',alpha=alphaVal)
    ax3 = ax1.twiny()
    ax3.hist(y,bins=bin_no,color=cy,orientation='horizontal',alpha=alphaVal)

    # Set the colors of the axis the same as histogram
    ax1.set_xlabel('x',color = 'b')
    ax1.set_ylabel('y',color = 'b')
    ax2.set_ylabel(r'No. of Occurrences',color=cx)
    ax2.tick_params('y',colors=cx)
    ax3.set_xlabel(r'No. of Occurrences',color=cy)
    ax3.tick_params('x',colors=cy)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
