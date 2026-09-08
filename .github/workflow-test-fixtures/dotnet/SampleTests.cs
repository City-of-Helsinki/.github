using Xunit;

namespace DotnetFixture;

public class SampleTests
{
    [Fact]
    public void Addition_ReturnsSum()
    {
        Assert.Equal(4, 2 + 2);
    }
}
