
import wmfbase, time

class wmfsource(object):
    def __init__(self, mf, deviceId):
        self.friendlyName = "Video source"
        self.deviceId = deviceId
        self.mf = mf
        self.device = self.mf.StartCamera(self.deviceId)
        
    def GetFrame(self):
        frame = self.mf.ProcessSamples(self.deviceId)
        return frame

class wmf(object):
    def __init__(self):
        self.mf = wmfbase.MediaFoundation()
        self.mf.Init()

    def __len__(self):
        deviceList = self.mf.ListDevices()
        return len(deviceList)

    def __getitem__(self, key):
        deviceList = self.mf.ListDevices()
        selectedDeviceInfo = deviceList[key]
        
        vidsrc = wmfsource(self.mf, selectedDeviceInfo[1])
        vidsrc.friendlyName = selectedDeviceInfo[0]
        return vidsrc

if __name__ == "__main__":
    wmfobj = wmf()
    print "Number of video sources", len(wmfobj)

    cam0 = wmfobj[0]

    print cam0.friendlyName    

    for i in range(100):
        frame = cam0.GetFrame()
        print frame.keys()
