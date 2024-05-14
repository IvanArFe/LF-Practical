// Generated from BoardGame.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BoardGameParser}.
 */
public interface BoardGameListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BoardGameParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BoardGameParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(BoardGameParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(BoardGameParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#game}.
	 * @param ctx the parse tree
	 */
	void enterGame(BoardGameParser.GameContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#game}.
	 * @param ctx the parse tree
	 */
	void exitGame(BoardGameParser.GameContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#gameType}.
	 * @param ctx the parse tree
	 */
	void enterGameType(BoardGameParser.GameTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#gameType}.
	 * @param ctx the parse tree
	 */
	void exitGameType(BoardGameParser.GameTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#move}.
	 * @param ctx the parse tree
	 */
	void enterMove(BoardGameParser.MoveContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#move}.
	 * @param ctx the parse tree
	 */
	void exitMove(BoardGameParser.MoveContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#player}.
	 * @param ctx the parse tree
	 */
	void enterPlayer(BoardGameParser.PlayerContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#player}.
	 * @param ctx the parse tree
	 */
	void exitPlayer(BoardGameParser.PlayerContext ctx);
	/**
	 * Enter a parse tree produced by {@link BoardGameParser#coordinate}.
	 * @param ctx the parse tree
	 */
	void enterCoordinate(BoardGameParser.CoordinateContext ctx);
	/**
	 * Exit a parse tree produced by {@link BoardGameParser#coordinate}.
	 * @param ctx the parse tree
	 */
	void exitCoordinate(BoardGameParser.CoordinateContext ctx);
}