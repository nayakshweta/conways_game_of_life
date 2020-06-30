using NUnit.Framework;

namespace Conways.Tests
{
    public class Tests
    {
        private Grid _grid;
        private string[] lines;
        [SetUp]
        public void Setup()
        {
            lines = Grid.ReadInputGridFromFile("/home/shwetn/workspace/csharpprac/conways/conways_game_of_life/C#/Conways/inputfile.txt");
        }

        [Test]
        public void ReadInputGridFromFile_LineMatches()
        {
            string[] FileLines = Grid.ReadInputGridFromFile("/home/shwetn/workspace/csharpprac/conways/conways_game_of_life/C#/Conways/inputfile.txt");
            Assert.AreEqual(FileLines[0], "........");
        }

        [Test]
        public void GridConstructor_GridCellsMatch()
        {
            _grid = new Grid(4, 8, lines);
            Assert.AreEqual(_grid[0,0], false);
            Assert.AreEqual(_grid[1,4], true);
            Assert.AreEqual(_grid[2,3], true);
        }


        [Test]
        public void DetermineNextGrid_ValueMatches()
        {
            _grid = new Grid(4, 8, lines);
            Grid nextGrid = _grid.DetermineNextGrid();
            Assert.AreEqual(nextGrid[1, 4], true);
            Assert.AreEqual(nextGrid[2, 4], true);
            Assert.AreEqual(nextGrid[2, 3], true);
            Assert.AreEqual(nextGrid[0, 0], false);
            Assert.AreEqual(nextGrid[0, 1], false);
            Assert.AreEqual(nextGrid[0, 2], false);
        }

        [Test]
        public void DetermineCellNeighbourCount_CountReturns3()
        {
            _grid = new Grid(4, 8, lines);
            int count = _grid.DetermineCellNeighbourCount(1, 3);
            Assert.AreEqual(count, 3);
        }

        [Test]
        public void GetCellNextState_NeighbourCount2CurrentStateAlive_ReturnsTrue()
        {
            _grid = new Grid(4, 8, lines);
            bool nextState = _grid.GetCellNextState(1, 3, 3);
            Assert.IsTrue(nextState);
        }
        
        [Test]
        public void GetCellNextState_NeighbourCount2CurrentStateDead_ReturnsFalse()
        {
            _grid = new Grid(4, 8, lines);
            bool nextState = _grid.GetCellNextState(3, 3, 2);
            Assert.IsFalse(nextState);
        }
    }
}