# Copyright 2024 The AI Edge Model Explorer Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Dict

from model_explorer import (Adapter, AdapterMetadata, ModelExplorerGraphs,
                            graph_builder)


class MyAdapter(Adapter):
    """A simple adapter that returns a hard-coded graph.

    See more info at:
    https://github.com/google-ai-edge/model-explorer/wiki/6.-Develop-Adapter-Extension
    """

    metadata = AdapterMetadata(id='my-adapter',
                               name='My first adapter',
                               description='My first adapter!',
                               source_repo='https://github.com/user/my_adapter',
                               fileExts=['test'])

    # This is required.
    def __init__(self):
        super().__init__()

    def convert(self, model_path: str, settings: Dict) -> ModelExplorerGraphs:

        # Create a graph for my road trip.
        graph = graph_builder.Graph(id='road_trip')

        ###################
        # Add nodes.

        # Create start and end node.
        #
        # They are located at root level hence the empty `namespace` parameter.

        # Create San Franciso as a sublayer of the CoastalDrive layer and add some
        # tourist sites there.
        G = graph_builder.GraphNode(id='g', label='G', namespace='')
        H = graph_builder.GraphNode(id='h', label='H', namespace='')
        C = graph_builder.GraphNode(id='c', label='C(s)', namespace='')
        pm = graph_builder.GraphNode(id='pm', label='+/-', namespace='')

        # Add all the nodes into graph.

        graph.nodes.extend(
            [G, H, C, pm])

        ###################
        # Add edges.
        H.incomingEdges.append(graph_builder.IncomingEdge(sourceNodeId='g'))
        pm.incomingEdges.append(graph_builder.IncomingEdge(sourceNodeId='h'))
        C.incomingEdges.append(graph_builder.IncomingEdge(sourceNodeId='g'))
        G.incomingEdges.append(graph_builder.IncomingEdge(sourceNodeId='pm'))

        return {'graphs': [graph]}
