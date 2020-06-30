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
            Assert.AreEqual(_grid[0,0], 0);
            Assert.AreEqual(_grid[1,4], 1);
            Assert.AreEqual(_grid[2,3], 1);
        }


        [Test]
        public void DetermineNextGrid_ValueMatches()
        {
            _grid = new Grid(4, 8, lines);
            Grid nextGrid = _grid.DetermineNextGrid();
            Assert.AreEqual(nextGrid[1, 4], 1);
            Assert.AreEqual(nextGrid[2, 4], 1);
            Assert.AreEqual(nextGrid[2, 3], 1);
            Assert.AreEqual(nextGrid[0, 0], 0);
            Assert.AreEqual(nextGrid[0, 1], 0);
            Assert.AreEqual(nextGrid[0, 2], 0);
        }

        public void DetermineCellNeighbourCount_CountReturns3()
        {
            _grid = new Grid(4, 8, lines);
            int count = _grid.DetermineCellNeighbourCount(1, 3);
            Assert.AreEqual(count, 3);
        }
    }
}