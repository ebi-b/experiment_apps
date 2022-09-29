
using System;
using System.IO;
using Tobii.Interaction;
using Tobii.Interaction.Framework;

namespace ConsoleApp5
{
    class Program
    {
        public static void Main()
        {
            Console.Write("In Eye Tracker");
            Start();
            while (true)
                Console.ReadKey();
        }
        public static void Start()
        {


            var host = new Host();
            host.Context.LaunchConfigurationTool(ConfigurationTool.CreateNewProfile, (data) => { });
            host.Context.LaunchConfigurationTool(ConfigurationTool.TestEyeTracking, (data) => { });
            host.Context.LaunchConfigurationTool(ConfigurationTool.SetupDisplay, (data) => { });
            host.Context.LaunchConfigurationTool(ConfigurationTool.RetailCalibration, (data) => { });

            var gazePointDataStream = host.Streams.CreateGazePointDataStream();
            var eyePositionDataStream = host.Streams.CreateEyePositionStream();
            var fixationDataStream = host.Streams.CreateFixationDataStream();
            var headPositionDataStream = host.Streams.CreateHeadPoseStream();

            // gazePointDataStream.GazePoint();
            String stateFileName = "States.txt";
            String path = "C:\\Engagement-Challenge Experiment\\EyeData";
            String gazefileName = "GazePoints.txt";
            String eyePositionFileName = "EyePositions.txt";
            String fixationDataFileName = "FixationData.txt";
            String headPositionDataFileName = "HeadPositions.txt";

            Directory.CreateDirectory(path);
            StreamWriter tmp0 = File.CreateText(path + "\\" + stateFileName);
            StreamWriter tmp1 = File.CreateText(path + "\\" + gazefileName);
            StreamWriter tmp2 = File.CreateText(path + "\\" + eyePositionFileName);
            StreamWriter tmp3 = File.CreateText(path + "\\" + fixationDataFileName);
            StreamWriter tmp4 = File.CreateText(path + "\\" + headPositionDataFileName);
            tmp0.Close();
            tmp1.Close();
            tmp2.Close();
            tmp3.Close();
            tmp4.Close();


            var dso = host.States.CreateDisplaySizeObserver();
            var etdso = host.States.CreateEyeTrackingDeviceStatusObserver();
            var gto = host.States.CreateGazeTrackingObserver();
            var sbo = host.States.CreateScreenBoundsObserver();
            var upo = host.States.CreateUserPresenceObserver();
            var upno = host.States.CreateUserProfileNameObserver();

            DateTime baseDate = new DateTime(1970, 1, 1);

            StreamWriter f0 = File.AppendText(Path.Combine(path + "\\" + stateFileName));


            if (dso.CurrentValue != null)
            {
                f0.WriteLine("Current Display Size is: " + dso.CurrentValue.ToString() + (DateTime.Now - baseDate).TotalMilliseconds);
                f0.Flush();
            }


            dso.WhenChanged(X => { f0.WriteLine("Display Size Changed to:" + X.ToString() + " TimeStamp:" + (DateTime.Now - baseDate).TotalMilliseconds); f0.Flush(); });
            etdso.WhenChanged(X => { f0.WriteLine("Eye Tracking Device Status Changed to:" + X.ToString() + " TimeStamp:" + (DateTime.Now - baseDate).TotalMilliseconds.ToString()); f0.Flush(); });
            gto.WhenChanged(X => {
                f0.WriteLine("Gaze Tracker Observer Status Changed to:" + X.ToString() + " TimeStamp:" + (DateTime.Now - baseDate).TotalMilliseconds.ToString()); f0.Flush();
            });
            sbo.WhenChanged(X => { f0.WriteLine("Screen Bound Changed to:" + X.ToString() + " TimeStamp:" + (DateTime.Now - baseDate).TotalMilliseconds.ToString()); f0.Flush(); });
            upo.WhenChanged(X => { f0.WriteLine("User Presence Observer Status Changed to:{0}, TimeStamp:{1}" + (DateTime.Now - baseDate).TotalMilliseconds.ToString()); f0.Flush(); });
            upno.WhenChanged(X => { f0.WriteLine("User Profile Name Obserever Status Changed to:" + X.ToString() + " TimeStamp:" + (DateTime.Now - baseDate).TotalMilliseconds.ToString()); f0.Flush(); });




            bool f1t = true;
            StreamWriter f1 = File.AppendText(Path.Combine(path + "\\" + gazefileName));
            gazePointDataStream.GazePoint((x, y, z) => {
                f1.WriteLine("X:{0}, Y:{1},TimeStamp:{2} ", x, y, z);
                if (f1t)
                {
                    f0.WriteLine("First Gaze Point Time: " + (DateTime.Now - baseDate).TotalMilliseconds);
                    f0.Flush();
                    f1t = false;
                }
            }
                );

            bool f2t = true;
            StreamWriter f2 = File.AppendText(Path.Combine(path + "\\" + eyePositionFileName));
            eyePositionDataStream.EyePosition(X => {
                f2.WriteLine("hasLeftEyePosition:{0}, hasRightEyePosition:{1}, leftEye:{2}, leftEyeNormalized:{3}, " +
                    "rightEye:{4}, rightEyeNormalized:{5}, timestamp:{6}, engineTimestamp:{7}"
                    , X.HasLeftEyePosition, X.HasRightEyePosition, X.LeftEye, X.LeftEyeNormalized, X.RightEye, X.RightEyeNormalized, X.Timestamp, X.EngineTimestamp);
                if (f2t)
                {
                    f0.WriteLine("First Eye Position Time: " + (DateTime.Now - baseDate).TotalMilliseconds);
                    f0.Flush();
                    f2t = false;
                }
            });

            bool f3t = true;
            StreamWriter f3 = File.AppendText(Path.Combine(path + "\\" + fixationDataFileName));
            fixationDataStream.Begin((x, y, z) => {
                f3.WriteLine("Begins, X:{0}, Y:{1},TimeStamp:{2} ", x, y, z);
                if (f3t)
                {
                    f0.WriteLine("First Begin Fixation time : " + (DateTime.Now - baseDate).TotalMilliseconds);
                    f0.Flush();
                    f3t = false;
                }

            });


            fixationDataStream.End((x, y, z) => f3.WriteLine("Ends, X:{0}, Y:{1},TimeStamp:{2} ", x, y, z));
            fixationDataStream.Data((x, y, z) => f3.WriteLine("Data, X:{0}, Y:{1},TimeStamp:{2} ", x, y, z));

            bool f4t = true;
            StreamWriter f4 = File.AppendText(Path.Combine(path + "\\" + headPositionDataFileName));
            headPositionDataStream.HeadPose((X, P, R) => {
                f4.WriteLine("TimeStamp:{0}, HeadPose:{1}, HeadRotation:{2} ", X, P, R);
                if (f4t)
                {
                    f0.WriteLine("First Head Pose Time: " + (DateTime.Now - baseDate).TotalMilliseconds);
                    f0.Flush();
                    f4t = false;
                }
            });

        }
    }
}
