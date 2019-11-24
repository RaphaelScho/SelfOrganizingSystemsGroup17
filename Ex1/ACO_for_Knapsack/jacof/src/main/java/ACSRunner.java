import java.io.IOException;

import org.apache.commons.cli.ParseException;
import org.apache.log4j.Logger;

import thiagodnf.jacof.aco.AntColonySystem;
import thiagodnf.jacof.problem.Problem;
import thiagodnf.jacof.problem.kp.KnapsackProblem;
import thiagodnf.jacof.problem.tsp.TravellingSalesmanProblem;
import thiagodnf.jacof.util.ExecutionStats;

public class ACSRunner {

	/** The class logger*/
	static final Logger LOGGER = Logger.getLogger(ACSRunner.class);
	
	public static void main(String[] args) throws ParseException, IOException {

		String instance = "src/main/resources/problems/kp/knapPI_2_1000_1000_1.kp";

		Problem problem = new KnapsackProblem(instance);

		AntColonySystem aco = new AntColonySystem(problem);

		aco.setNumberOfAnts(100);
		aco.setNumberOfIterations(500);
		aco.setAlpha(1.0);
		aco.setBeta(5.0);
		aco.setRho(0.8);
		aco.setOmega(0.8);
		aco.setQ0(0.6);

		ExecutionStats es = ExecutionStats.execute(aco, problem);
		es.printStats();
	}

}
