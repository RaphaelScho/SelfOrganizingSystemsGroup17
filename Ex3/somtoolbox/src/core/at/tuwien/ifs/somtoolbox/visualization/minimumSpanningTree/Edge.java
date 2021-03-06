/*
 * Copyright 2004-2010 Information & Software Engineering Group (188/1)
 *                     Institute of Software Technology and Interactive Systems
 *                     Vienna University of Technology, Austria
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.ifs.tuwien.ac.at/dm/somtoolbox/license.html
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package at.tuwien.ifs.somtoolbox.visualization.minimumSpanningTree;

/**
 * Represents an Edge in a (directed) graph
 * 
 * @author Thomas Kern
 * @author Magdalena Widl
 * @version $Id: Edge.java 4295 2014-01-09 01:22:47Z mayer $
 */
public class Edge implements Comparable<Edge> {

    private Node start;

    private Node end;

    private double weight;

    public Edge(Node start, Node end, double weight) {
        this.start = start;
        this.end = end;
        this.weight = weight;
    }

    public Node getEnd() {
        return end;
    }

    public Node getStart() {
        return start;
    }

    public double getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return "(" + start.getLabel() + "," + end.getLabel() + ")";
    }

    @Override
    public int compareTo(Edge o) {
        if (o == null) {
            return 1;
        } else {
            return Double.compare(getWeight(), o.getWeight());
        }
    }
}
