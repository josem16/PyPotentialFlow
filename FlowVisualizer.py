import numpy as np
import matplotlib.pyplot as plt

class FlowVisualizer(object):
    """
    """

    def __init__(self):
        self.axes_limits = None
        self.potential_flows = {}

        self.groups = []
        self.group_to_id_map = {}
        self.id_to_group_map = {}

        self.flow_types = []
        self.flow_type_to_id_map = {}
        self.id_to_flow_type_map = {}

        self.id_counter = 1

    def add_potential_flow(self, potential_flow, group=0):
        """
        Add potential flow class object.

        Parameters
        ----------
        potential_flow: class [Uniform2D, Source2D, Doublet2D, Vortex]
            Potential flows class object.
        group: int, optional, default: 0
            Group tag to associate with potential flow class object.
        """
        # Add potential flow
        self.potential_flows[self.id_counter] = potential_flow

        # Add group/ID pair
        self.id_to_group_map[self.id_counter] = group
        self._add_group_id_pair(group)

        # Add flow type/ID pair
        self.id_to_flow_type_map[self.id_counter] = potential_flow.flow_type
        self._add_flow_type_id_pair(potential_flow.flow_type)

        # Increment id counter
        self.id_counter += 1

    def _add_group_id_pair(self, group):
        """
        Add group/ID pair to class dictionary.
        """
        # Create new group tag if it does not exist
        if group not in self.groups:
            self.group_to_id_map[group] = []

        # Add group/ID pair
        self.group_to_id_map[group].append(self.id_counter)

    def _add_flow_type_id_pair(self, flow_type):
        """
        Add flow type/ID pair to class dictionary.
        """
        # Create new flow type tag if it does not exist
        if flow_type not in self.flow_types:
            self.flow_type_to_id_map[flow_type] = []

        # Add flow type/ID pair
        self.flow_type_to_id_map[flow_type].append(self.id_counter)

    def remove_potential_flow(self, flow_id):
        """
        Remove potential flow class object.

        Parameters
        ----------
        flow_id: int
            ID associated with potential flows class object.
        """
        # Remove potential flow
        self.potential_flows.pop(flow_id)

        # Remove group/ID pair
        group_temp = self.id_to_group_map[flow_id]
        self.group_to_id_map[group_temp].remove(flow_id)
        self.id_to_group_map.pop(flow_id)

        # Remove flow type/ID pair
        flow_type_temp = self.id_to_flow_type_map[flow_id]
        self.flow_type_to_id_map[flow_type_temp].remove(flow_id)
        self.id_to_flow_type_map.pop(flow_id)

    def get_velocity(self, xVals, yVals, group=None, flow_type=None):
        """
        Computes the velocity induced at a point(s)
        """
        Vx_tot = np.zeros(xVals.shape)
        Vy_tot = np.zeros(yVals.shape)
        for flow_id, potential_flow in self.potential_flows.iteritems():
            # Check if id is valid
            isvalid = self._check_id_in_group_and_type(flow_id, group=group, flow_type=flow_type)

            if isvalid == True:
                # Compute velocity
                Vx, Vy = potential_flow.get_velocity(xVals, yVals)

                # Increment total velocities
                Vx_tot += Vx
                Vy_tot += Vy

        return Vx_tot, Vy_tot

    def get_stream_function(self, xVals, yVals, group=None, flow_type=None):
        """
        Computes the stream function at a point(s)
        """
        psi_tot = np.zeros(xVals.shape)
        for flow_id, potential_flow in self.potential_flows.iteritems():
            # Check if id is valid
            isvalid = self._check_id_in_group_and_type(flow_id, group=group, flow_type=flow_type)

            if isvalid == True:
                # Compute velocity
                psi = potential_flow.get_stream_function(xVals, yVals)

                # Increment total velocities
                psi_tot += psi

        return psi_tot

    def get_velocity_potential(self, xVals, yVals, group=None, flow_type=None):
        """
        Computes the veocity potential at a point(s)
        """
        phi_tot = np.zeros(xVals.shape)
        for flow_id, potential_flow in self.potential_flows.iteritems():
            # Check if id is valid
            isvalid = self._check_id_in_group_and_type(flow_id, group=group, flow_type=flow_type)

            if isvalid == True:
                # Compute velocity
                psi = potential_flow.get_velocity_potential(xVals, yVals)

                # Increment total velocities
                phi_tot += phi

        return phi_tot

    def _check_id_in_group_and_type(self, flow_id, group=None, flow_type=None):
        """
        Check if id is in specified group and flow type.
        """
        # Valid group ids
        if group is not None:
            valid_group_ids = self.group_to_id_map[group]
        else:
            valid_group_ids = range(self.id_counter)

        # Valid flow type ids
        if flow_type is not None:
            valid_flow_type_ids = self.flow_type_to_id_map[flow_type]
        else:
            valid_flow_type_ids = range(self.id_counter)

        # Check if flow id is valid
        valid_ids = list(set().union(valid_group_ids, valid_flow_type_ids))
        if flow_id in valid_ids:
            return True
        else:
            return False

    def plot_potential_flows(self):
        return

    def plot_streamlines(self):
        return

    def plot_pressure_distribution(self):
        return
