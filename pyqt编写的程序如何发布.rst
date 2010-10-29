2009年12月3号研究了一下如何发布pyqt的程序，整理内容如下：

pyqt是qt图形库对于python编程语言的一个绑定，qt是著名的跨平台图形开发库，专业，易用，以及企业级别支持，文档齐全。python是一个简单易用的解释语言。不过这篇文章是关于如何发布pyqt程序的，那么读者应该都知道这些，我就不多介绍了。

我们用pyqt开发完程序的时候，得到的是一堆python源代码，以及一些资源文件，比如用到的图片，声音什么的。程序在我们开发平台上可以运行，但是我们还需要想办法让客户机也能够用我们的代码。

我们需要做2件事情：一个是把源代码打包成可以放到任何电脑都能够执行的程序，另一个是做一个安装程序，好方便安装到客户机上。

我现在选择py2exe作为打包的工具，nsis作为生成安装程序的工具。

py2exe

* `py2exe教程1 <http://www.cppblog.com/len/archive/2008/08/11/58547.html>`_ 
* `py2exe官方教程 <http://www.py2exe.org/index.cgi/Tutorial>`_
* `py2exe下载 <http://sourceforge.net/projects/py2exe/files/>`_

nsis

* `nsis教程 <http://www.52z.com/soft/16497.html>`_
* `nsis官方教程 <http://nsis.sourceforge.net/Simple_tutorials>`_
* `nsis下载 <http://nsis.sourceforge.net/Download>`_

nsis下载后文档中有详细的介绍，安装目录中含有许多的示例。

我写的示例在 `这里 <http://dl.dropbox.com/u/1167873/others/test_pyqt.zip>`_

稍微解释一下：
比如，我写了一个新的专案，名称叫test_pyqt，新建了一个这样的文件夹。
里面有一个main.py源代码。同时还有一个res的资源目录。
为了能够利用py2exe打包，需要新建一个setup.py的设置文件。

几个难点整理如下：
根据py2exe里面说的，pyqt需要包含sip（我也不知道这是什么东西，估计是C++转python的时候要用到的。。），下面的脚本含有具体的设置。
编译好的文件还需要一些额外的dll文件（主要是针对没有加sp的XP版本运行时出现“程序出错”报错的状况），放在dll文件夹里面，打包的时候要加上（dll文件在上面的示例中）。我没有研究出如何把这些文件加到可执行文件里面的办法，如果你知道的话，就告诉我。

内容如下::

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    # ---------------------------------
    # 打包程序
    
    from distutils.core import setup
    import py2exe,glob
    
    setup(windows=[{
                    "script": 'main.py',
                    #应用程序图标
                    "icon_resources":[(1, "res/py.ico")] }],
          data_files=[
                      #资源文件
                      ("res", glob.glob("res/*.*")),
                      #因为客户机可能缺少部分开发文件造成无法运行程序，需要打包一些文件
                      (".",glob.glob("dlls/*.*")),
                      ],
          options={"py2exe":{"includes":["sip"],
                             "optimize":2,
                             #打包成一个文件，加快读取速度
                             "compressed":1,
                             "bundle_files":2,
                             #文件放在哪里
                             "dist_dir":"temp/dist",
                             #少了个文件,不管它
                             "dll_excludes":["MSVCP90.dll"],
                             },
                   },
          zipfile=None,)#一个文件
    
    #删除build临时目录
    import shutil
    shutil.rmtree('build')
    
执行::

    python setup.py py2exe

以上语句需要把python的目录加到path里面去，或者你可以在python前加上完整的python安装目录.
我是加path的，因为这样使用python更方便。

之后，会生成temp/dist文件夹，里面就是一个main.exe可执行文件了，还有res文件夹。

之后是生成安装文件，新建一个installer.nsi文件，内容如下（因为比较长，放到最后）。

内容比较多。当时我在做的时候，看了很多的文档才知道具体怎么做。为了方便，你还是用我的示例吧。

下面的内容含有多语言，license页面，安装内容页面，安装目录页面，以及反安装页面。

如果你感兴趣的话可以自己研究，我是被nsis细节给累倒了。

这个文件你只需要改下面软件名称的部分，它会自动把dist打包安装到program files里面，生成执行文件链接到桌面以及菜单项中。

对了，主执行文件的入口是main.py这个源代码。

文件写好后，鼠标右键菜单中有一个compile nsis script的选项，点击就可以生成安装文件。

具体的细节可以看我上面示例的压缩文档。我写了一个makefile来方便快速执行操作（别告诉我你不会用make）。
该示例在windows xp,python2.6,nsis2.46,pyqt4.5,py2exe上测试通过。等以后考虑跨平台版本::

    #coding:utf-8
    
    ;软件名称
    !define NAME "test_pyqt"
    
    ;主执行文件
    !define EXE "dist\main.exe"
    
    ;样式
    XPstyle on
    
    ;输出的安装文件
    OutFile "temp/${NAME}_installer.exe"
    
    ;默认目录
    InstallDir $PROGRAMFILES\${NAME}
    
    ; 检查是否已经安装过
    InstallDirRegKey HKLM "Software\${NAME}" "Install_Dir"
    
    ;需要管理员权限
    RequestExecutionLevel admin
    
    ;--------------------------------
    
    ; 页面
    
    Page license
    Page components
    Page directory
    Page instfiles
    
    UninstPage uninstConfirm
    UninstPage instfiles
    
    ;--------------------------------
    
    ; 安装主目录
    Section "main"
    
    SectionIn RO
    
    ; Set output path to the installation directory.
    SetOutPath $INSTDIR
    
    ; 需要安装的程序
    File /r "temp\dist"
    
    ; Write the installation path into the registry
    WriteRegStr HKLM SOFTWARE\${NAME} "Install_Dir" "$INSTDIR"
    
    ; Write the uninstall keys for Windows
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "DisplayName" "${NAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "UninstallString" '"$INSTDIR\uninstall.exe"'
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}" "NoRepair" 1
    WriteUninstaller "uninstall.exe"
    
    SectionEnd
    
    ; 开始菜单
    Section "开始菜单"
    
    CreateDirectory "$SMPROGRAMS\${NAME}"
    CreateShortCut "$SMPROGRAMS\${NAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
    SetOutPath $INSTDIR\dist
    CreateShortCut "$SMPROGRAMS\${NAME}\${NAME}.lnk" "$INSTDIR\${EXE}" "" "$INSTDIR\${EXE}" 0
    
    SectionEnd
    
    ; 桌面快捷方式
    Section "桌面快捷方式"
    SetOutPath $INSTDIR\dist
    CreateShortCut "$DESKTOP\${NAME}.lnk" "$INSTDIR\${EXE}" "" "$INSTDIR\${EXE}" 0
    SectionEnd
    
    ;--------------------------------
    
    ; Uninstaller
    
    Section "Uninstall"
    
    ; Remove registry keys
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\"
    DeleteRegKey HKLM SOFTWARE\${NAME}
    
    ; Remove directories used
    Delete "$DESKTOP\${NAME}.lnk"
    RMDir /r "$SMPROGRAMS\${NAME}"
    RMDir /r "$INSTDIR"
    
    SectionEnd
    
    ;--------------------------------
    ; 语言部分
    ; First is default
    LoadLanguageFile "${NSISDIR}\Contrib\Language files\English.nlf"
    LoadLanguageFile "${NSISDIR}\Contrib\Language files\SimpChinese.nlf"
    
    ; License data
    ; Not exactly translated, but it shows what's needed
    LicenseLangString myLicenseData ${LANG_ENGLISH} "license.txt"
    LicenseLangString myLicenseData ${LANG_SIMPCHINESE} "license.txt"
    LicenseData $(myLicenseData)
    
    ; Set name using the normal interface (Name command)
    ; LangString Name ${LANG_ENGLISH} "English"
    ; LangString Name ${LANG_SIMPCHINESE} "Simplified Chinese"
    ; Name $(Name)
    
    ;--------------------------------
    Function .onInit
    
    ;Language selection dialog
    
    Push ""
    Push ${LANG_ENGLISH}
    Push English
    Push ${LANG_SIMPCHINESE}
    Push "Simplified Chinese"
    Push A ; A means auto count languages
    ; for the auto count to work the first empty push (Push "") must remain
    LangDLL::LangDialog "Installer Language" "Please select the language of the installer"
    
    Pop $LANGUAGE
    StrCmp $LANGUAGE "cancel" 0 +2
    Abort
    FunctionEnd
    [/sourcecode]
                
2010/10/29修改: 其实现在pyinstaller用起来更方便, 直接build就可以了. python2.6以后的版本需要下载开发版本使用.
