import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 600
    height: 600
    title: mainViewModel.map_name ? mainViewModel.map_name : qsTr("heat map")

    Shortcut {
        sequence: "Ctrl+Q"
        onActivated: { Qt.quit() }
    }

    Shortcut {
        sequence: "Ctrl+O"
        onActivated: { fileDialog.open() }
    }

    FileDialog {
        id: fileDialog
        title: "Choose a map folder"
        selectFolder: true
        selectExisting: true
        onAccepted: { mainViewModel.map_dir = fileUrl }
    }

    GridLayout {
        id: mainGrid
        anchors.fill: parent
        anchors.leftMargin: 10
        anchors.rightMargin: 10
        anchors.bottomMargin: 10
        rows: 2
        columns: 2

        StackLayout {
            Layout.row: 1
            Layout.column: 1
            Layout.columnSpan: 2
            Layout.fillWidth: true
            Layout.fillHeight: true

            Blend {
                anchors.fill: parent
                cached: false
                source: previewImage
                foregroundSource: heatmapImage
                mode: "normal"
                antialiasing: true
                smooth: true
            }
            Image {
                id: heatmapImage
                anchors.fill: parent
                source: mainViewModel.map_dir ? "image://heatmap/" + mainViewModel.map_dir + "?dot_size=" + dotSizeSlider.value + "&flip=" + mainViewModel.flip + "&opacity=" + opacitySlider.value: ""
                fillMode: Image.PreserveAspectFit
                antialiasing: true
                smooth: true
                visible: false
            }
            Image {
                id: previewImage
                anchors.fill: parent
                source: mainViewModel.preview ? mainViewModel.preview : ""
                fillMode: Image.PreserveAspectFit
                antialiasing: true
                smooth: true
                visible: false
            }
        }

        RowLayout {
            Layout.row: 2
            Layout.column: 1
            Layout.fillWidth: true

            IconButton {
                text: "Open map folder"
                icon: "open.svg"
                onClicked: { fileDialog.open() }
            }

            Label { text: "Dot size" }
            Slider {
                id: dotSizeSlider
                from: 1
                to: mainViewModel.map_size / 2
                value: mainViewModel.dot_size
                stepSize: 1
                snapMode: Slider.SnapAlways

                Layout.fillWidth: true
                onValueChanged: { mainViewModel.dot_size = value }
            }
        }

        RowLayout {
            Layout.row: 2
            Layout.column: 2
            Layout.fillWidth: true

            Label { text: "Opacity" }
            Slider {
                id: opacitySlider
                from: 0
                to: 255
                stepSize: 1
                value: 200

                Layout.fillWidth: true
            }
            IconButton {
                text: "Mirror"
                icon: "mirror.svg"
                onClicked: { heatmapImage.mirror = !heatmapImage.mirror }
            }
            IconButton {
                text: "Flip"
                icon: "flip.svg"
                onClicked: { mainViewModel.flip = !mainViewModel.flip }
            }
        }
    }
}
