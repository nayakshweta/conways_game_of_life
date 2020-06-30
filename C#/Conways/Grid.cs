using System;
using System.IO;
using System.Collections.ObjectModel;

namespace Conways
{
    public class Grid
    {
        bool[,] _inputGrid;
        public int Rows {get; private set;}
        public int Columns {get; private set;}
        public Grid(int rows, int columns, string[] lines)
        {
            Rows = rows;
            Columns = columns;
            if (lines.Length != rows) 
                throw new System.ArgumentException("Row count does not match.", "rows");

            bool[,] grid = new bool[Rows,Columns];

            for(int i=0; i<Rows; i++)
            {
                if (lines[i].Length != columns) 
                    throw new System.ArgumentException("Column count does not match the content of the lines provided", "columns");
                for(int j=0; j<Columns; j++)
                {
                    char input = lines[i][j];

                    if (input == '.') grid[i, j] = false;
                    else if (input == '*') grid[i, j] = true;
                    else throw new System.ArgumentException("Character provided does not match", "lines");
                }
            }
            _inputGrid=grid;
        }

        public static string[] ReadInputGridFromFile(string filename)
        {
            return File.ReadAllLines(filename);
        }

        public Grid DetermineNextGrid()
        {
            string dummyLine = new string('.', Columns);
            string[] dummyFile = new string[Rows];
            for (int i=0; i<Rows; i++)
            {
                dummyFile.SetValue(dummyLine, i);
            }
            Grid newGrid = new Grid(Rows, Columns, dummyFile);
            for (int i=0; i<Rows; i++)
            {
                for (int j=0; j<Columns; j++)
                {
                    int neighbourCount = DetermineCellNeighbourCount(i, j);
                    newGrid[i, j] = GetCellNextState(i, j, neighbourCount);
                }
            }
            return newGrid;
        }

        public int DetermineCellNeighbourCount(int x, int y)
        {
            int neighbourCount = 0;
            for (int i=x-1; i<=x+1; i++)
            {
                for (int j=y-1; j<=y+1; j++)
                {
                    if (i>=0 && j>=0 && i<Rows && j<Columns && !(i==x && j==y))
                    {
                        if (_inputGrid[i,j]==true) neighbourCount++;
                    }
                }
            }
            return neighbourCount;
        }

        public bool GetCellNextState(int x, int y, int neighbourCount)
        {
            if ((neighbourCount==2 || neighbourCount==3) && _inputGrid[x, y]==true) 
                return true;
            else if (neighbourCount==3 && _inputGrid[x, y]==false) 
                return true;
            else 
                return false;
        }

        public override string ToString()
        {
            string retGrid = "";
            for (int i=0; i<Rows; i++)
            {
                for (int j=0; j<Columns; j++)
                {
                    if (_inputGrid[i,j] == true) 
                        retGrid += "*";
                    else if (_inputGrid[i,j] == false) 
                        retGrid += ".";
                }
                retGrid += "\n";
            }
            return retGrid;
        }
        public bool this[int i, int j]
        {
            get
            {
                return _inputGrid[i, j];
            }
            set{
                _inputGrid[i, j] = value;
            }
        }
    }
}