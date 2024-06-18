namespace TODO
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            AddButton.Click += AddButton_Click;
            DeleteButton.Click += DeleteButton_Click;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void AddButton_Click(object sender, EventArgs e)
        {
            string newItem = textBox1.Text;
            if (!string.IsNullOrWhiteSpace(newItem))
            {
                listBox1.Items.Add(newItem);
                textBox1.Clear();
            }
        }

        private void DeleteButton_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex != -1)
            {
                listBox1.Items.RemoveAt(listBox1.SelectedIndex);
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
