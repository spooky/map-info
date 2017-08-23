import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 600
    height: 600
    title: mainViewModel.map_name ? mainViewModel.map_name : qsTr("heat map")

    Shortcut {
        sequence: "Ctrl+Q"
        onActivated: {
            fileDialog.close()
            mainWindow.close()
            Qt.quit()
        }
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

        Image {
            id: heatmapImage
            source: mainViewModel.map_dir ? "image://heatmap/" + mainViewModel.map_dir + "?dot_size=" + dotSizeSlider.value + "&flip=" + mainViewModel.flip : ""
            fillMode: Image.PreserveAspectFit
            opacity: opacitySlider.value

            Layout.row: 1
            Layout.column: 1
            Layout.columnSpan: 2
            Layout.fillWidth: true
            Layout.fillHeight: true
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
                to: mainViewModel.map_size
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
                to: 1
                stepSize: 0.01
                value: 1

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
