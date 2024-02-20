import "package:flutter/material.dart";
import "package:google_maps_flutter/google_maps_flutter.dart";

class FlightHistory extends StatefulWidget {
  final LatLng? flightLocation;

  const FlightHistory({Key? key, this.flightLocation}) : super(key: key);

  @override
  _FlightHistoryState createState() => _FlightHistoryState();
}

class _FlightHistoryState extends State<FlightHistory> {
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
        title: Text("Last Flight"),
      ),
      body: Container(
        padding: EdgeInsets.all(16.0),
        child: ListView.builder(
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
      ),
    );
  }
}
