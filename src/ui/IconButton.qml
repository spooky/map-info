import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3

ToolButton {
    id: btn
    property alias icon: image.source

    implicitWidth: 32
    implicitHeight: 32
    padding: 4

    ToolTip.visible: down
    ToolTip.text: btn.text

    contentItem: Image {
        id: image
        mipmap: true
        fillMode: Image.PreserveAspectFit
    }
}
