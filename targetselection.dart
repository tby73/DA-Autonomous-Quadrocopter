import "package:flutter/material.dart";
import "package:google_maps_flutter/google_maps_flutter.dart";
import "package:geolocator/geolocator.dart";
import "homescreen.dart";

class MapScreen extends StatefulWidget {
  @override
  _MapScreenState createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  Set<Marker> _markers = {};
  LatLng? _flightLocation;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Target Selection"),
      ),
      body: GoogleMap(
        initialCameraPosition:
            CameraPosition(target: LatLng(37.42, -122), zoom: 14.0),
        markers: _markers,
        onTap: (LatLng position) {
          setState(() {
            _markers.add(Marker(
              markerId: MarkerId("SELECTED_TARGET_LABEL"),
              position: position,
              infoWindow: InfoWindow(
                title: 'TARGET',
                snippet:
                    'Lat: ${position.latitude}, Lng: ${position.longitude}',
              ),
              icon: BitmapDescriptor.defaultMarker,
              onTap: () {
                // Handle marker label tap if needed
              },
            ));
          });
        },
        buildingsEnabled: true,
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          print("DRONE_STATUS: LAUNCH");
          _flightLocation =
              _markers.isNotEmpty ? _markers.first.position : null;
          _navigateToHomeScreen(context);
        },
        label: Text("Start Flight"),
        icon: Icon(Icons.flight),
        backgroundColor: Colors.black,
      ),
    );
  }

  void _navigateToHomeScreen(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(
          builder: (context) => HomeScreen(flightLocation: _flightLocation)),
    );
  }
}
