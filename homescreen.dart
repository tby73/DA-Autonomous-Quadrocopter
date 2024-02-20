import "package:flutter/material.dart";
import "package:google_maps_flutter/google_maps_flutter.dart";
import "targetselection.dart";
import "camera.dart";
import "flighthistory.dart";

class HomeScreen extends StatefulWidget {
  final LatLng? flightLocation;

  const HomeScreen({Key? key, this.flightLocation}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<LatLng> flightLocations = [];

  @override
  void initState() {
    super.initState();
    if (widget.flightLocation != null) {
      flightLocations.add(widget.flightLocation!);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Icon(
              Icons.blur_circular,
              color: Colors.white,
            ),
            SizedBox(width: 8),
            Text(
              "AutoQuad Control Center",
              style: TextStyle(
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: Icon(Icons.account_circle_outlined),
            onPressed: () {
              // Add onPressed functionality for the profile icon if needed
            },
          ),
        ],
      ),
      body: Padding(
          padding: EdgeInsets.all(10.0),
          child: Column(
            children: [
              Row(
                children: [
                  MaterialButton(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    onPressed: () {},
                    color: Colors.black,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.wifi_find_outlined,
                          size: 36,
                          color: Colors.white,
                        ),
                        SizedBox(height: 8),
                        Text(
                          "Connect to Drone ROS",
                          style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    minWidth: 180,
                    height: 150,
                  ),
                  SizedBox(width: 10),
                  MaterialButton(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    onPressed: () {
                      _navigateToMap(context);
                    },
                    color: Colors.black,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.map,
                          size: 36,
                          color: Colors.white,
                        ),
                        SizedBox(
                          height: 8,
                        ),
                        Text(
                          "Target Selection",
                          style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    minWidth: 180,
                    height: 150,
                  ),
                ],
              ),
              SizedBox(height: 10.0),
              Row(
                children: [
                  MaterialButton(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    onPressed: () {},
                    color: Colors.black,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.video_camera_back,
                          size: 36,
                          color: Colors.white,
                        ),
                        SizedBox(height: 8),
                        Text(
                          "Camera",
                          style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    minWidth: 180,
                    height: 150,
                  ),
                  SizedBox(width: 10),
                  MaterialButton(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(25.0),
                    ),
                    onPressed: () {
                      _navigateToFlightHistory(context);
                    },
                    color: Colors.black,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.history,
                          size: 36,
                          color: Colors.white,
                        ),
                        SizedBox(height: 8),
                        Text(
                          "Recent Flights",
                          style: TextStyle(color: Colors.white),
                        ),
                      ],
                    ),
                    minWidth: 180,
                    height: 150,
                  ),
                ],
              ),
              SizedBox(height: 10.0),
              Text("Last Flight:"),
              SizedBox(height: 10.0),
              Container(
                padding: EdgeInsets.all(16.0),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey),
                  borderRadius: BorderRadius.circular(8.0),
                ),
                child: ListView.builder(
                  shrinkWrap: true,
                  itemCount: flightLocations.length,
                  itemBuilder: (context, index) {
                    return ListTile(
                      leading: Icon(Icons.flight),
                      trailing: Icon(Icons.keyboard_arrow_right),
                      title: Text("Last Flight"),
                      subtitle: Text(
                        'Destination: LAT ${flightLocations[index].latitude}, LONG ${flightLocations[index].longitude}',
                      ),
                    );
                  },
                ),
              )
            ],
          )),
    );
  }

  void _navigateToMap(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => MapScreen()),
    );
  }

  void _navigateToCamera(BuildContext context) {
    Navigator.push(context, MaterialPageRoute(builder: (context) => Camera()));
  }

  void _navigateToFlightHistory(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
          builder: (context) =>
              FlightHistory(flightLocation: widget.flightLocation)),
    );
  }
}
