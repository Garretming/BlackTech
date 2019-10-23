
alias
# 自定义IP地址
alias myip="ifconfig en0 | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'"
Xcode执行shell脚本
在 Xcode 工程对应 Target的Build Phases中新增Run Scrpit Phase(还可以改名字Generating image plist) → 点+号 → New Run Script Phase

为脚本增加执行权限chmod 755 file.sh 或 chmod u+xfile.sh
sh file.sh



Xcode Run Script Phase
和一般的shell没有太大的区别，但是多了很多环境变量。

可以添加一个 Run Script,添加一条命令

env
输出这些环境变量，结果如下(通过 Xcode -> View -> Navigators -> Show the Report navigator 查看)

HEADERMAP_INCLUDES_PROJECT_HEADERS=YES
AUTOJUMP_ERROR_PATH=/Users/yunmai/Library/autojump/errors.log
COPY_PHASE_STRIP=NO
JAVA_ZIP_FLAGS=-urg
ENABLE_STRICT_OBJC_MSGSEND=YES
LOCAL_APPS_DIR=/Applications
SDK_PRODUCT_BUILD_VERSION=15C107
REMOVE_CVS_FROM_RESOURCES=YES
SED=/usr/bin/sed
EXECUTABLES_FOLDER_PATH=Demo.app/Executables
TARGET_DEVICE_OS_VERSION=11.2
SYSTEM_DEVELOPER_UTILITIES_DIR=/Applications/Xcode.app/Contents/Developer/Applications/Utilities
ENABLE_ON_DEMAND_RESOURCES=YES
PRESERVE_DEAD_CODE_INITS_AND_TERMS=NO
SYSTEM_DEVELOPER_TOOLS_RELEASENOTES_DIR=/Applications/Xcode.app/Contents/Developer/ADC Reference Library/releasenotes/DeveloperTools
PRODUCT_NAME=Demo
UNLOCALIZED_RESOURCES_FOLDER_PATH=Demo.app
TEMP_FILES_DIR=/Users/yunmai/Library/Developer/Xcode/DerivedData/Demo-berndezuxwjamydzcmytratqdchj/Build/Intermediates.noindex/Demo.build/Debug-iphonesimulator/Demo.build
SWIFT_PLATFORM_TARGET_PREFIX=ios
LD_GENERATE_MAP_FILE=NO
DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
USE_DYNAMIC_NO_PIC=YES
LIBRARY_FLAG_NOSPACE=YES
REZ_COLLECTOR_DIR=/Users/yunmai/Library/Developer/Xcode/DerivedData/Demo-berndezuxwjamydzcmytratqdchj/Build/Intermediates.noindex/Demo.build/Debug-iphonesimulator/Demo.build/ResourceManagerResources
TERM_PROGRAM=Apple_Terminal
DEVELOPER_SDK_DIR=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs

...

PRODUCT_SETTINGS_PATH=/Users/yunmai/Workspace/DYYFloatWindow/Demo/Info.plist
BUILD_ROOT=/Users/yunmai/Library/Developer/Xcode/DerivedData/Demo-berndezuxwjamydzcmytratqdchj/Build/Products
USE_HEADERMAP=YES
_=/usr/bin/env
可以在脚本中直接使用这些变量。

// bundle id
PRODUCT_BUNDLE_IDENTIFIER 

// info.plist 的位置
INFOPLIST_PATH

// 工程根目录
SRCROOT
常用的 Run Script
Build Number 自增

设置只在Release configuration 下自增

 if [ $CONFIGURATION == Release ]; then
     echo "Bumping build number..."
     plist=${PROJECT_DIR}/${INFOPLIST_FILE}
     
     #increment the build number (ie 115 to 116)
     buildnum=$(/usr/libexec/PlistBuddy -c "Print CFBundleVersion" "${plist}")
     
     if [[ "${buildnum}" == "" ]]; then
         echo "No build number in $plist"
         exit 2
     fi
 
     buildnum=$(expr $buildnum + 1)
 
     /usr/libexec/Plistbuddy -c "Set CFBundleVersion $buildnum" "${plist}"
 
     echo "Bumped build number to $buildnum"
 
 else
     echo $CONFIGURATION " build - Not bumping build number."
 fi
Bugly 自动上传dSYMs

打包上传时移除第三方库中无用的部分

# Without further ado, here’s the script. Add a Run Script step to your build steps, put it after your step to embed frameworks, set it to use /bin/sh and enter the following script:

APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"

# This script loops through the frameworks embedded in the application and
# removes unused architectures.
find "$APP_PATH" -name '*.framework' -type d | while read -r FRAMEWORK
do
FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)
FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"
echo "Executable is $FRAMEWORK_EXECUTABLE_PATH"

EXTRACTED_ARCHS=()

for ARCH in $ARCHS
do
echo "Extracting $ARCH from $FRAMEWORK_EXECUTABLE_NAME"
lipo -extract "$ARCH" "$FRAMEWORK_EXECUTABLE_PATH" -o "$FRAMEWORK_EXECUTABLE_PATH-$ARCH"
EXTRACTED_ARCHS+=("$FRAMEWORK_EXECUTABLE_PATH-$ARCH")
done

echo "Merging extracted architectures: ${ARCHS}"
lipo -o "$FRAMEWORK_EXECUTABLE_PATH-merged" -create "${EXTRACTED_ARCHS[@]}"
rm "${EXTRACTED_ARCHS[@]}"

echo "Replacing original executable with thinned version"
rm "$FRAMEWORK_EXECUTABLE_PATH"
mv "$FRAMEWORK_EXECUTABLE_PATH-merged" "$FRAMEWORK_EXECUTABLE_PATH"

done