from PyQt5.QtWidgets import(QWidget, QApplication, QVBoxLayout,
                            QSlider, QProgressBar, QTabWidget)

app = QApplication([])
window = QWidget()

tab1 = QWidget()
slider = QSlider()
progress = QProgressBar()
progress.setValue(0) 

v1 = QVBoxLayout()
v1.addWidget(slider)
v1.addWidget(progress)
tab1.setLayout(v1)

slider.valueChanged.connect(lambda value:progress.setValue(value))

tabs = QTabWidget()
tabs.addTab(tab1, 'Вкладка 1')

v2 = QVBoxLayout()
v2.addWidget(tabs)
window.setLayout(v2)

window.show()
app.exec_()
